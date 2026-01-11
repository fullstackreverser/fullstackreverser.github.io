#!/usr/bin/env bash
set -euo pipefail

if [ "$#" -eq 0 ]; then
  read -r -p "Title: " title
else
  title="$*"
fi

if [ -z "${title}" ]; then
  echo "Title is required." >&2
  exit 1
fi

date_str=$(date "+%Y-%m-%d %H:%M:%S %z")
date_prefix=$(date "+%Y-%m-%d")
slug=$(printf '%s' "$title" | tr '[:upper:]' '[:lower:]' | sed -E 's/[^a-z0-9]+/-/g; s/^-+|-+$//g')

if [ -z "${slug}" ]; then
  echo "Could not derive a slug from the title." >&2
  exit 1
fi

file="_posts/${date_prefix}-${slug}.md"

if [ -e "$file" ]; then
  echo "File exists: $file" >&2
  exit 1
fi

cat > "$file" <<TEMPLATE
---
title: ${title}
date: ${date_str}
categories: []
tags: []     # TAG names should always be lowercase
published: true
---

# Overview
TEMPLATE

echo "Created $file"
