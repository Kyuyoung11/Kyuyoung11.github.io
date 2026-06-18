import os
import re
import json
import base64
import time
import requests
from datetime import datetime, timezone, timedelta

# ── 설정 ──────────────────────────────────────────────────────────────
GEMINI_API_KEY = os.environ["GEMINI_API_KEY"]
GITHUB_TOKEN   = os.environ["GITHUB_TOKEN"]
GITHUB_REPO    = "Kyuyoung11/Kyuyoung11.github.io"
BRANCH         = "master"
POSTS_PATH     = "_posts"

KST = timezone(timedelta(hours=9))
TODAY = datetime.now(KST).strftime("%Y-%m-%d")

# ── 1. Gemini로 최신 IT 기술동향 뉴스 수집 + 포스트 생성 ──────────────
def generate_post() -> dict:
    """Gemini에게 최신 IT 기술동향을 검색하고 블로그 포스트로 작성 요청"""

    prompt = f"""
오늘({TODAY}) 기준 최신 IT 기술동향 뉴스를 조사하고, Jekyll 블로그용 마크다운 포스트를 작성해줘.

블로그 카테고리: News (IT 기술동향 뉴스를 정리하는 카테고리)

주제: AI 모델/서비스 업데이트, 개발 자동화 도구, LLM 활용 사례, 클라우드 AI 서비스, 오픈소스 AI, 개발자 생산성 도구 등

조건:
- 실제 최근 뉴스/트렌드를 기반으로 작성 (가능한 한 최신 정보 반영)
- 포스트는 800~1200자 분량
- 독자는 AI 및 자동화에 관심 있는 개발자
- 딱딱하지 않고 읽기 쉽게
- 소제목(##)을 2~3개 사용해 구조화

아래 JSON 형식으로만 응답해. 다른 텍스트 없이 JSON만:
{{
  "title": "포스트 제목 (한국어, [IT동향] 접두사 포함)",
  "tags": ["tag1", "tag2", "tag3"],
  "content": "마크다운 본문 내용 (front matter 제외)"
}}
"""

    models = ["gemini-2.0-flash-lite", "gemini-2.0-flash"]
    payload = {
        "contents": [{"parts": [{"text": prompt}]}],
        "generationConfig": {"temperature": 0.7}
    }

    resp = None
    for attempt, model in enumerate(models):
        url = f"https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent?key={GEMINI_API_KEY}"
        for retry in range(3):
            resp = requests.post(url, json=payload, timeout=60)
            if resp.status_code == 429:
                wait = 30 * (retry + 1)
                print(f"⚠️  429 Too Many Requests ({model}), {wait}초 후 재시도...")
                time.sleep(wait)
                continue
            break
        if resp.status_code != 429:
            break
        print(f"⚠️  {model} 한도 초과, 다음 모델로 전환...")

    resp.raise_for_status()

    raw = resp.json()["candidates"][0]["content"]["parts"][0]["text"]

    # JSON 파싱 (코드블록 제거)
    raw = re.sub(r"```json|```", "", raw).strip()
    return json.loads(raw)


# ── 2. Jekyll front matter + 본문 조합 ────────────────────────────────
def build_markdown(post: dict) -> str:
    tags_str = "\n".join(f"  - {t}" for t in post["tags"])
    front_matter = f"""---
layout: post
title:  "{post['title']}"
categories:
  - News
date:   {TODAY}
tags:
{tags_str}
---
"""
    return front_matter + "\n" + post["content"]


# ── 3. GitHub API로 직접 커밋 ─────────────────────────────────────────
def commit_to_github(filename: str, content: str):
    api_url = f"https://api.github.com/repos/{GITHUB_REPO}/contents/{POSTS_PATH}/{filename}"
    headers = {
        "Authorization": f"token {GITHUB_TOKEN}",
        "Accept": "application/vnd.github.v3+json"
    }

    encoded = base64.b64encode(content.encode("utf-8")).decode("utf-8")

    # 파일이 이미 존재하면 sha 필요 (덮어쓰기 방지용 — 보통 새 파일이라 불필요)
    check = requests.get(api_url, headers=headers)
    sha = check.json().get("sha") if check.status_code == 200 else None

    payload = {
        "message": f"[auto] IT 기술동향 포스트 - {TODAY}",
        "content": encoded,
        "branch": BRANCH,
    }
    if sha:
        payload["sha"] = sha

    resp = requests.put(api_url, headers=headers, json=payload)
    resp.raise_for_status()
    print(f"✅ 커밋 완료: {filename}")
    print(f"   URL: https://kyuyoung11.github.io")


# ── 메인 ──────────────────────────────────────────────────────────────
if __name__ == "__main__":
    print(f"📰 {TODAY} IT 기술동향 포스트 생성 중...")

    post = generate_post()
    print(f"📝 제목: {post['title']}")

    markdown = build_markdown(post)

    # 파일명: YYYY-MM-DD-제목슬러그.md
    slug = re.sub(r"[^\w\s-]", "", post["title"].lower())
    slug = re.sub(r"[\s]+", "-", slug)[:50]
    filename = f"{TODAY}-{slug}.md"

    commit_to_github(filename, markdown)
