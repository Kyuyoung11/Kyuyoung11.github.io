# CLAUDE.md

이 파일은 이 저장소에서 작업하는 Claude Code(claude.ai/code)에게 가이드를 제공합니다.

## 오류 확인

오류 발생 시 `C:\project\error_info\` 경로에 텍스트 파일 또는 이미지로 오류 내용을 저장해 둔다. 오류 디버깅 요청 시 이 경로를 먼저 확인할 것.

## 명령어


```bash
# 의존성 설치
bundle install

# 로컬 실행 (http://localhost:4000 에서 서빙)
bundle exec jekyll serve

# 정적 사이트 빌드
bundle exec jekyll build
```

## 아키텍처

Jekyll 기반 개인 개발 블로그로, GitHub Pages(https://kyuyoung11.github.io/)에 배포됩니다. Flexton 테마를 커스터마이징하여 사용하며 한국어로 작성된 콘텐츠를 담고 있습니다.

### 레이아웃 계층 구조

- `_layouts/default.html` — 전체를 감싸는 HTML 기본 틀
- `_layouts/home.html` — default 확장; 사이드바 + 메인 콘텐츠 영역 렌더링
- `_layouts/post.html` — home 확장; 자동 생성 목차(`_includes/toc.html`)와 관련 글 포함하여 게시글 렌더링
- `_layouts/category-page.html` — home 확장; 카테고리별 게시글 목록 렌더링

### 주요 파일

- `_config.yml` — 사이트 전체 설정 (제목, 작성자, 애널리틱스, 페이지네이션, 퍼머링크 형식)
- `_includes/nav_list_main` — 사이드바 카테고리 네비게이션 (확장자 없음); 각 카테고리명과 URL이 하드코딩되어 있음
- `_data/navigation.yml` — 상단 네비게이션 바 링크
- `_plugins/category-generator.rb` — Jekyll 카테고리별로 `/category/<slug>/index.html` 페이지를 자동 생성하는 플러그인

### 게시글 작성

게시글은 `_posts/<서브디렉토리>/YYYY-MM-DD-slug.md` 경로에 위치합니다. 서브디렉토리는 파일 정리용이며, 실제 카테고리 소속은 front matter의 `categories:` 필드로 결정됩니다.

기본 게시글 front matter:
```yaml
---
layout: post
title: "..."
categories:
  - Java      # 사이드바에 표시되는 상위 카테고리
  - Spring    # 하위 카테고리
tags: [Spring, 인프런]
toc: true
toc_sticky: true
date: YYYY-MM-DD
last_modified_at: YYYY-MM-DD
---
```

`_config.yml`에 `future: true`가 설정되어 있어, 미래 날짜의 게시글도 즉시 게시됩니다.

### 새 카테고리 추가

두 가지 작업이 필요합니다(`_data/navigation.yml` 주석에도 명시되어 있음):

1. `_includes/nav_list_main`에 기존 패턴을 따라 항목 추가 (`category[0] == "카테고리명"` 을 체크하는 Liquid 루프).
2. `_pages/category/<Category>.md` 파일 생성 — `layout: category-page`, `permalink: category/<slug>/`, `sidebar_main: true` 설정.
