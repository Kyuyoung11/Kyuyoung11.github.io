# 규의 개발 블로그

> **[kyuyoung11.github.io](https://kyuyoung11.github.io/)** — Jekyll 기반 개인 기술 블로그

## 소개

Java, Spring, SQL, React 등 개발 학습 내용을 정리하고, AI/자동화 관련 최신 IT 기술동향을 매일 자동 포스팅하는 블로그입니다.

---

## 아키텍처

```
┌─────────────────────────────────────────────────────────────────────┐
│                       자동 포스팅 파이프라인                           │
│                                                                     │
│  GitHub Actions (매일 09:00 KST)                                    │
│         │                                                           │
│         ▼                                                           │
│  auto_post.py ──── GitHub API로 최근 7일 포스트 조회 (중복 방지)        │
│         │                                                           │
│         ▼                                                           │
│  Claude Haiku API ──── IT 기술동향 포스트 생성 (800~1200자)            │
│         │                                                           │
│         ▼                                                           │
│  GitHub API ──── _posts/news/ 에 직접 커밋 → 자동 배포               │
└─────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────┐
│                        Jekyll 블로그 구조                             │
│                                                                     │
│  _posts/          ← 마크다운 게시글 (카테고리별 서브디렉토리)             │
│  _layouts/        ← default → home → post / category-page          │
│  _includes/       ← nav_list_main (사이드바), toc.html (목차)        │
│  _plugins/        ← category-generator.rb (카테고리 페이지 자동 생성)  │
│  _config.yml      ← 사이트 전체 설정                                  │
│       │                                                             │
│       ▼                                                             │
│  bundle exec jekyll build → _site/                                  │
└─────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────┐
│                          배포 & 외부 연동                             │
│                                                                     │
│  GitHub Pages ──── kyuyoung11.github.io                            │
│  Flexton 테마  ──── 커스터마이징 CSS / Liquid                          │
│  Google Analytics ─ 방문자 트래킹 (G-H0EJMY0THF)                    │
└─────────────────────────────────────────────────────────────────────┘
```

---

## 기술 스택

| 분류 | 기술 |
|------|------|
| 정적 사이트 생성 | [Jekyll](https://jekyllrb.com/) + Ruby + Bundler |
| 마크다운 처리 | kramdown |
| 테마 | [Flexton](https://github.com/artemsheludko/flexton) (커스터마이징) |
| 호스팅 | GitHub Pages |
| 자동 포스팅 | GitHub Actions + Python + Claude Haiku API |
| 검색 | Simple-Jekyll-Search |
| 분석 | Google Analytics |

---

## 주요 기능

- **자동 IT 기술동향 포스팅**: 매일 Claude AI가 최신 IT 뉴스를 요약해 자동으로 포스트를 생성·커밋합니다. 최근 7일간 다룬 주제와 겹치지 않도록 중복 방지 로직이 적용되어 있습니다.
- **카테고리 네비게이션**: `_plugins/category-generator.rb`가 카테고리별 페이지를 자동으로 생성하고, 사이드바에서 게시글 수와 함께 표시됩니다.
- **자동 목차(TOC)**: `_includes/toc.html`이 게시글의 헤딩을 파싱해 목차를 자동 생성합니다.
- **미래 날짜 게시글 지원**: `_config.yml`의 `future: true` 설정으로 미래 날짜의 게시글도 즉시 게시됩니다.

---

## 카테고리

| 카테고리 | 설명 |
|---------|------|
| Java | Java 기초 & 중급 |
| Spring | Spring Framework 학습 |
| TDD | TDD & Clean Code |
| SQL | SQL 쿼리 & 튜닝 |
| React | React 프론트엔드 |
| AI | AI 자동화, Claude Code |
| News | IT 기술동향 (자동 포스팅) |
| GitBlog | 블로그 운영 기록 |
| Tool | 개발 도구 팁 |
| Conference | 개발 컨퍼런스 후기 |

---

## 로컬 실행

```bash
# 의존성 설치
bundle install

# 로컬 서버 실행 (http://localhost:4000)
bundle exec jekyll serve

# 정적 사이트 빌드
bundle exec jekyll build
```

---

## 게시글 작성

게시글은 `_posts/<서브디렉토리>/YYYY-MM-DD-slug.md` 경로에 작성합니다.

```yaml
---
layout: post
title: "제목"
categories:
  - Java      # 상위 카테고리
  - Spring    # 하위 카테고리
tags: [Spring, 인프런]
toc: true
toc_sticky: true
date: YYYY-MM-DD
last_modified_at: YYYY-MM-DD
---
```

### 새 카테고리 추가 시

1. `_includes/nav_list_main` — 사이드바에 항목 추가
2. `_pages/category/<Category>.md` — 카테고리 페이지 파일 생성

---

## 라이선스

테마 원작자: [Artem Sheludko](https://github.com/artemsheludko/flexton)
