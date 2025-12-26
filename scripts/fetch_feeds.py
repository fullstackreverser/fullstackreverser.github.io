import os, re, json, hashlib, datetime
from pathlib import Path

import yaml
import feedparser

ROOT = Path(__file__).resolve().parents[1]
POSTS = ROOT / "_posts"
CACHE_DIR = ROOT / ".cache"
SEEN_FILE = CACHE_DIR / "seen.json"
FEEDS_FILE = ROOT / "scripts" / "feeds.yml"

def slugify(s: str) -> str:
    s = s.lower().strip()
    s = re.sub(r"[^\w\s-]", "", s)
    s = re.sub(r"[\s_-]+", "-", s)
    return s[:80].strip("-")

def load_seen():
    if SEEN_FILE.exists():
        return set(json.loads(SEEN_FILE.read_text(encoding="utf-8")))
    return set()

def save_seen(seen):
    CACHE_DIR.mkdir(parents=True, exist_ok=True)
    SEEN_FILE.write_text(json.dumps(sorted(seen)), encoding="utf-8")

def entry_key(entry) -> str:
    # RSS마다 id/guid가 없을 수도 있으니 link+title로 fallback
    base = (getattr(entry, "id", "") or "") + "|" + (getattr(entry, "link", "") or "") + "|" + (getattr(entry, "title", "") or "")
    return hashlib.sha256(base.encode("utf-8")).hexdigest()

def main():
    POSTS.mkdir(parents=True, exist_ok=True)
    conf = yaml.safe_load(FEEDS_FILE.read_text(encoding="utf-8"))
    feeds = conf.get("feeds", [])

    seen = load_seen()
    new_entries = []

    for f in feeds:
        d = feedparser.parse(f["url"])
        for e in d.entries[:30]:  # 너무 많이 쌓이지 않게 제한
            k = entry_key(e)
            if k in seen:
                continue
            seen.add(k)
            new_entries.append((f["name"], e))

    if not new_entries:
        print("No new entries.")
        save_seen(seen)
        return

    today = datetime.date.today().isoformat()
    ts = datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S +0000")

    # 하루에 1개 포스트로 묶기(권장). 원하면 엔트리마다 1포스트로 바꿀 수도 있음.
    title = f"Daily Security Feed - {today}"
    filename = f"daily-security-feed-{today}.md"
    path = POSTS / filename

    lines = []
    lines.append("---")
    lines.append(f'title: "{title}"')
    lines.append(f"date: {ts}")
    # lines.append("layout: post")
    lines.append("categories: [security, feeds]")
    lines.append("tags: [security, feeds]")
    lines.append("published: true")
    lines.append("---\n")
    lines.append(f"## Security Feed Digest ({today})\n")

    # 소스별로 보기 좋게
    from collections import defaultdict
    grouped = defaultdict(list)
    for source, e in new_entries:
        grouped[source].append(e)

    for f in feeds:
        source = f["name"]
        if source not in grouped:
            continue
        lines.append(f"### {source}\n")
        for e in grouped[source]:

    # for source in sorted(grouped.keys()):
    #     lines.append(f"### {source}\n")
    #     for e in grouped[source]:
            t = getattr(e, "title", "Untitled")
            link = getattr(e, "link", "")
            published = getattr(e, "published", "") or getattr(e, "updated", "")
            if published:
                lines.append(f"- [{t}]({link}) — {published}")
            else:
                lines.append(f"- [{t}]({link})")
        lines.append("")

    # 같은 날짜 포스트가 이미 있으면 append로 누적(원하면 overwrite)
    if path.exists():
        old = path.read_text(encoding="utf-8")
        # 기존 헤더 유지하고 아래에 이어붙이기(간단 처리)
        path.write_text(old + "\n" + "\n".join(lines[lines.index("## Security Feed Digest ("+today+")\n"):]), encoding="utf-8")
    else:
        path.write_text("\n".join(lines), encoding="utf-8")

    save_seen(seen)
    print(f"Wrote: {path}")

if __name__ == "__main__":
    main()
