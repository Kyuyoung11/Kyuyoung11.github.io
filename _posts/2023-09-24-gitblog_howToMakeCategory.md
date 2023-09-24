---
layout: post
title: "[GitBlog] 블꾸 (3) - 카테고리 사이드바 만들기"
categories: 
  - GitBlog

tags: [Blog, Git, Profile, Jekyll, Flexton]
toc: true
toc_sticky : true
date: 2023-09-24
last_modified_at: 2023-09-24

---



---
카테고리는 역시 프로필 아래에 있어야 편한 것 같아서 추가하기로 결정

---
## 1. 포스트 머릿말에 카테고리 작성 확인
````markdown
layout: post
title: "[GitBlog] 블꾸 (3) - 카테고리 만들기"

categories: GitBlog << 이 부분

tags: [Blog, Git, Profile, Jekyll]
toc: true
toc_sticky : true
date: 2023-09-24
last_modified_at: 2023-09-24
````

---

## 2. 프로젝트에서 div id 검색해서, css 파일에 set 해주기
div id인 c-wrap-content 에다가 table 설정 내용을 넣어주면 됨~
```` css
.c-wrap-content {
  padding: 20px;
  background-color: $white-color;
  table {
    display: block;
    margin-bottom: 1em;
    width: 100%;
    font-family: $base-font-family;
    font-size: $base-font-size;
    border-collapse: collapse;
    overflow-x: auto;

    & + table {
      margin-top: 1em;
    }
  }

  thead {
    background-color: $sub-background;
    border-bottom: 2px solid mix(#000, $border-color-post, 25%);
  }

  th {
    padding: 0.5em;
    font-weight: bold;
    text-align: center;
  }

  td {
    padding: 0.5em;
    border-bottom: 1px solid mix(#000, $border-color-post, 25%);
  }

  tr,
  td,
  th {
    vertical-align: middle;
  }
}
````

테이블 템플릿은 구글링해서 css 코드 가져오면 편함  
나는 너무나도 감사한 깃블로그의 테이블 css 코드 오려옴  
[https://ansohxxn.github.io/blog/public/](https://ansohxxn.github.io/blog/public/)

---
## 3. 적용 후
![]({{site.baseurl}}/images/230920/after.PNG)

---

## 참고 사이트
[Github 블로그] minimal-mistake 블로그 카테고리 만들기 (+ 전체 글 수) - [https://ansohxxn.github.io/blog/category/](https://ansohxxn.github.io/blog/category/)  
[minimal-mistakes] 카테고리(category) 만들기 [https://x2info.github.io/minimal-mistakes/%EC%B9%B4%ED%85%8C%EA%B3%A0%EB%A6%AC_%EB%A7%8C%EB%93%A4%EA%B8%B0/](https://x2info.github.io/minimal-mistakes/%EC%B9%B4%ED%85%8C%EA%B3%A0%EB%A6%AC_%EB%A7%8C%EB%93%A4%EA%B8%B0/)
---

## 앞으로 하고싶은거
* ~~색 커스텀~~
* ~~폰트크기 조정~~
* ~~포스트 목록 커스텀~~
* ~~표 커스텀~~
* 글자간격 조정
* 통계 페이지 추가
* 아카이브 페이지 추가
* 카테고리
* 목차

아자아자!