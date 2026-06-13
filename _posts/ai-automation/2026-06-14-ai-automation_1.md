---
layout: post
title: "[AI Automation] GitHub Actions + Gemini API로 블로그 자동 포스팅 구축하기"
categories:
  - AI
  - AI Automation
tags: [GitHub Actions, Gemini, Python, 자동화, Jekyll]
toc: true
toc_sticky: true
date: 2026-06-14
last_modified_at: 2026-06-14
---

> 매일 IT 기술동향 뉴스 글을 자동으로 블로그에 올려주는 파이프라인을 구축했다.  
> GitHub Actions + Python + Gemini API 조합으로, 매일 아침 자동으로 글이 올라오도록 설계했다. 실제로 잘 동작하는지는 좀 더 지켜봐야 할 것 같다.

<br>

---
## 어떤 걸 만들었나

Jekyll 기반 깃블로그에 **IT 기술동향 뉴스 글을 자동으로 생성 + 커밋**하는 파이프라인이다.

흐름은 이렇다:

```
GitHub Actions (매일 KST 09:00)
  → Python 스크립트 실행
    → Gemini API 호출 (뉴스 조사 + 마크다운 포스트 생성)
    → GitHub API로 _posts/ 에 직접 커밋
      → Jekyll 빌드 → 블로그 자동 배포
```

따로 서버를 운영하거나 크론탭을 관리할 필요 없이, GitHub 인프라 위에서 모든 게 돌아가도록 설계했다.

<br><br>

---
## 구성 파일

```
.github/
└── workflows/
    ├── auto-post.yml   # GitHub Actions 워크플로우 정의
    └── auto_post.py    # 포스트 생성 + 커밋 스크립트
```

<br>

### auto-post.yml

```yaml
name: IT 기술동향 자동 포스팅

on:
  schedule:
    - cron: '0 0 * * *'   # 매일 UTC 00:00 = KST 09:00
  workflow_dispatch:        # 수동 실행도 가능

jobs:
  post:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: '3.11'
      - run: pip install requests
      - name: 포스트 생성 및 커밋
        env:
          GEMINI_API_KEY: ${{ secrets.GEMINI_API_KEY }}
          GITHUB_TOKEN:   ${{ secrets.GITHUB_TOKEN }}
        run: python auto_post.py
```

워크플로우 자체는 단순하다. Python 환경 세팅 후 스크립트 하나 실행하는 게 전부다.  
`GEMINI_API_KEY`는 GitHub 레포 Settings → Secrets에 등록해두면 된다.

<br>

### auto_post.py 핵심 로직

**1. Gemini API로 포스트 생성**

```python
def generate_post() -> dict:
    prompt = f"""
오늘({TODAY}) 기준 최신 IT 기술동향 뉴스를 조사하고, Jekyll 블로그용 마크다운 포스트를 작성해줘.
블로그 카테고리: News (IT 기술동향 뉴스를 정리하는 카테고리)
...
JSON 형식으로만 응답해:
{{
  "title": "포스트 제목 (한국어, [IT동향] 접두사 포함)",
  "tags": ["tag1", "tag2", "tag3"],
  "content": "마크다운 본문 내용"
}}
"""
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key={GEMINI_API_KEY}"
    resp = requests.post(url, json={"contents": [{"parts": [{"text": prompt}]}]}, timeout=60)
    raw = resp.json()["candidates"][0]["content"]["parts"][0]["text"]
    raw = re.sub(r"```json|```", "", raw).strip()
    return json.loads(raw)
```

Gemini에게 JSON 형식으로만 응답하도록 지시해서, 파싱이 쉽게 되도록 했다.  
코드블록(`` ```json ```)이 붙어서 나오는 경우가 있어서 정규식으로 제거하는 처리도 추가했다.

<br>

**2. Jekyll front matter 조합**

```python
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
```

<br>

**3. GitHub API로 직접 커밋**

```python
def commit_to_github(filename: str, content: str):
    api_url = f"https://api.github.com/repos/{GITHUB_REPO}/contents/{POSTS_PATH}/{filename}"
    encoded = base64.b64encode(content.encode("utf-8")).decode("utf-8")
    payload = {
        "message": f"[auto] IT 기술동향 포스트 - {TODAY}",
        "content": encoded,
        "branch": BRANCH,
    }
    requests.put(api_url, headers=headers, json=payload)
```

`git clone` + `git commit` + `git push` 없이, GitHub REST API로 파일을 직접 올린다.  
Actions 워크플로우에서 기본으로 제공되는 `GITHUB_TOKEN`을 그대로 쓰면 되기 때문에 별도 PAT 발급도 필요 없다.

<br><br>

---
## 카테고리 구조

이 자동화 작업을 기록하면서 블로그 카테고리도 정리했다.

```
AI
  └── Claude Code      # Claude Code 관련 개발 경험
  └── AI Automation    # AI 자동화 구축 기록 (이 글)

News                   # Gemini가 매일 자동 생성하는 IT동향 뉴스
```

자동 생성 뉴스 글은 `News` 카테고리로, 자동화를 직접 구축하는 과정은 `AI Automation` 카테고리로 분리했다.

<br><br>

---
## 마치며

세팅 자체는 완료했고, 매일 아침 자동으로 글이 올라오는 구조로 만들었다.  
실제로 잘 돌아가는지는 며칠 지켜보면서 확인해볼 예정이다.

Gemini API 무료 티어 기준으로 하루 한 번 호출이면 비용 부담은 없을 것 같고, 잘 된다면 뉴스 퀄리티를 높이는 방향(Grounding 활용, 여러 기사 크롤링 후 요약 등)도 시도해볼 것 같다.

<br><br>
