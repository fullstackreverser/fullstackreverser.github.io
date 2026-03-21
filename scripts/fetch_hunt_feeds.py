"""
Daily Hunt Feed — MITRE ATT&CK TTP 기반 Threat Hunt OSINT 피드 수집기

흐름:
  1. enterprise-attack.json에서 attack-pattern 기법 이름 + T-번호 인덱스 빌드
  2. feeds.yml의 RSS 소스에서 엔트리 수집 (dedup: hunt_seen.json)
  3. 2단계 필터링
       1차: RSS title + summary에서 TTP 키워드 매칭 (HTTP 없음)
       2차: 1차 통과한 기사의 실제 URL fetch → 본문에서 최종 TTP 매칭
  4. 매칭된 TTP 목록과 함께 daily-hunt-feed 포스트 생성
"""

import os, re, json, hashlib, datetime, html
from pathlib import Path
from collections import defaultdict
from html.parser import HTMLParser

import yaml
import feedparser
import requests

ROOT = Path(__file__).resolve().parents[1]
POSTS = ROOT / "_posts"
CACHE_DIR = ROOT / ".cache"
SEEN_FILE = CACHE_DIR / "hunt_seen.json"
FEEDS_FILE = ROOT / "scripts" / "feeds.yml"
ATTACK_FILE = ROOT / "scripts" / "enterprise-attack.json"

FETCH_TIMEOUT = 10  # seconds per article request
MAX_ENTRIES_PER_FEED = 30
USER_AGENT = "Mozilla/5.0 (compatible; ThreatHuntBot/1.0)"


# ── HTML 텍스트 추출기 ─────────────────────────────────────────────────────────

class _TextExtractor(HTMLParser):
    def __init__(self):
        super().__init__()
        self._buf = []
        self._skip = False

    def handle_starttag(self, tag, attrs):
        if tag in ("script", "style", "noscript"):
            self._skip = True

    def handle_endtag(self, tag):
        if tag in ("script", "style", "noscript"):
            self._skip = False

    def handle_data(self, data):
        if not self._skip:
            self._buf.append(data)

    def get_text(self):
        return " ".join(self._buf)


def html_to_text(raw_html: str) -> str:
    p = _TextExtractor()
    try:
        p.feed(raw_html)
    except Exception:
        pass
    return p.get_text()


# ── ATT&CK 인덱스 빌드 ────────────────────────────────────────────────────────

def build_ttp_index(attack_file: Path) -> list[dict]:
    """
    enterprise-attack.json에서 attack-pattern만 추출.
    반환값: [{"id": "T1566", "name": "Phishing", "tactic": "initial-access"}, ...]
    """
    raw = json.loads(attack_file.read_text(encoding="utf-8"))
    techniques = []
    for obj in raw.get("objects", []):
        if obj.get("type") != "attack-pattern":
            continue
        if obj.get("x_mitre_deprecated", False) or obj.get("revoked", False):
            continue

        # External ID (T-number)
        tech_id = ""
        for ref in obj.get("external_references", []):
            if ref.get("source_name") == "mitre-attack":
                tech_id = ref.get("external_id", "")
                break
        if not tech_id:
            continue

        name = obj.get("name", "").strip()
        tactics = [
            phase["phase_name"]
            for phase in obj.get("kill_chain_phases", [])
            if phase.get("kill_chain_name") == "mitre-attack"
        ]

        techniques.append({
            "id": tech_id,
            "name": name,
            "tactic": tactics[0] if tactics else "",
        })

    print(f"[ATT&CK] {len(techniques)} techniques loaded.")
    return techniques


def build_keyword_map(techniques: list[dict]) -> dict[str, dict]:
    """
    키워드(소문자) → technique 정보 딕셔너리.
    기법 이름과 T-번호 모두 키워드로 등록.
    """
    kmap = {}
    for t in techniques:
        # 기법 이름 (소문자)
        kmap[t["name"].lower()] = t
        # T-번호 (대소문자 무관하게 매칭하기 위해 소문자로 저장)
        kmap[t["id"].lower()] = t
    return kmap


def match_ttps(text: str, kmap: dict[str, dict]) -> list[dict]:
    """
    텍스트에서 TTP 키워드 매칭. 중복 제거 후 반환.
    """
    text_lower = text.lower()
    matched = {}
    for keyword, technique in kmap.items():
        # 단어 경계 매칭으로 오탐 감소
        if re.search(r"\b" + re.escape(keyword) + r"\b", text_lower):
            matched[technique["id"]] = technique
    return list(matched.values())


# ── dedup 캐시 ────────────────────────────────────────────────────────────────

def load_seen() -> set:
    if SEEN_FILE.exists():
        return set(json.loads(SEEN_FILE.read_text(encoding="utf-8")))
    return set()


def save_seen(seen: set):
    CACHE_DIR.mkdir(parents=True, exist_ok=True)
    SEEN_FILE.write_text(json.dumps(sorted(seen)), encoding="utf-8")


def entry_key(entry) -> str:
    base = (
        (getattr(entry, "id", "") or "")
        + "|"
        + (getattr(entry, "link", "") or "")
        + "|"
        + (getattr(entry, "title", "") or "")
    )
    return hashlib.sha256(base.encode("utf-8")).hexdigest()


# ── 기사 본문 fetch ───────────────────────────────────────────────────────────

def fetch_article_text(url: str) -> str:
    """URL의 본문을 가져와 plain text로 반환. 실패 시 빈 문자열."""
    try:
        resp = requests.get(
            url,
            timeout=FETCH_TIMEOUT,
            headers={"User-Agent": USER_AGENT},
            allow_redirects=True,
        )
        if resp.status_code == 200:
            return html_to_text(resp.text)
    except Exception as e:
        print(f"  [WARN] fetch failed ({url}): {e}")
    return ""


# ── slugify ───────────────────────────────────────────────────────────────────

def slugify(s: str) -> str:
    s = s.lower().strip()
    s = re.sub(r"[^\w\s-]", "", s)
    s = re.sub(r"[\s_-]+", "-", s)
    return s[:80].strip("-")


# ── 메인 ─────────────────────────────────────────────────────────────────────

def main():
    POSTS.mkdir(parents=True, exist_ok=True)

    # 1. ATT&CK 인덱스 빌드
    print("[*] Building ATT&CK TTP index...")
    techniques = build_ttp_index(ATTACK_FILE)
    kmap = build_keyword_map(techniques)

    # 2. RSS 수집
    conf = yaml.safe_load(FEEDS_FILE.read_text(encoding="utf-8"))
    feeds = conf.get("feeds", [])
    seen = load_seen()

    candidates = []  # (source_name, entry) — 1차 통과
    for f in feeds:
        print(f"[*] Fetching RSS: {f['name']}")
        d = feedparser.parse(f["url"])
        for e in d.entries[:MAX_ENTRIES_PER_FEED]:
            k = entry_key(e)
            if k in seen:
                continue
            seen.add(k)

            # 1차: RSS title + summary 키워드 체크
            rss_text = " ".join([
                getattr(e, "title", "") or "",
                getattr(e, "summary", "") or "",
            ])
            if match_ttps(rss_text, kmap):
                candidates.append((f["name"], e))

    print(f"[*] 1st-pass candidates: {len(candidates)}")

    # 3. 2차 필터 — 실제 기사 본문 fetch + 최종 TTP 매칭
    results = []  # (source_name, entry, matched_ttps)
    for source, e in candidates:
        url = getattr(e, "link", "") or ""
        title = getattr(e, "title", "Untitled")
        print(f"  [fetch] {title[:60]}")

        article_text = fetch_article_text(url) if url else ""
        full_text = " ".join([
            getattr(e, "title", "") or "",
            getattr(e, "summary", "") or "",
            article_text,
        ])
        matched = match_ttps(full_text, kmap)
        if matched:
            results.append((source, e, matched))

    print(f"[*] 2nd-pass results: {len(results)}")

    save_seen(seen)

    if not results:
        print("No TTP-matched entries.")
        return

    # 4. 포스트 생성
    today = datetime.date.today().isoformat()
    ts = datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S +0000")
    title = f"Daily Hunt Feed - {today}"
    filename = f"{today}-daily-hunt-feed.md"
    path = POSTS / filename

    lines = []
    lines.append("---")
    lines.append(f'title: "{title}"')
    lines.append(f"date: {ts}")
    lines.append("categories: [security, hunt]")
    lines.append("tags: [threat-hunting, ttp, mitre-attack]")
    lines.append("published: true")
    lines.append("---\n")
    lines.append(f"## Threat Hunt Feed ({today})\n")

    grouped = defaultdict(list)
    for source, e, matched in results:
        grouped[source].append((e, matched))

    for f in feeds:
        source = f["name"]
        if source not in grouped:
            continue
        lines.append(f"### {source}\n")
        for e, matched in grouped[source]:
            t = getattr(e, "title", "Untitled")
            link = getattr(e, "link", "")
            published = getattr(e, "published", "") or getattr(e, "updated", "")

            # TTP 태그 포맷: "Phishing (T1566), Valid Accounts (T1078)"
            ttp_tags = ", ".join(
                f"{m['name']} ({m['id']})" for m in matched
            )

            entry_line = f"- [{t}]({link})"
            if published:
                entry_line += f" — {published}"
            lines.append(entry_line)
            lines.append(f"  - **Matched TTPs:** {ttp_tags}")
        lines.append("")

    digest_header = f"## Threat Hunt Feed ({today})\n"
    if path.exists():
        old = path.read_text(encoding="utf-8")
        idx = lines.index(digest_header)
        path.write_text(old + "\n" + "\n".join(lines[idx:]), encoding="utf-8")
    else:
        path.write_text("\n".join(lines), encoding="utf-8")

    print(f"Wrote: {path}")


if __name__ == "__main__":
    main()
