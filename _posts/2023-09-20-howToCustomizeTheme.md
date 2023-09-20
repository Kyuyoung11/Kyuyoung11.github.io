---
layout: post
title: "[Jekyll] 깃 블로그 꾸미기(블꾸) (2) - 표 디자인 변경"
categories: Jekyll

tags: [Blog, Git, Profile]
toc: true
toc_sticky : true
date: 2023-09-20
last_modified_at: 2023-09-20

---



---
글에 들어가는 표가 테두리가 없음   
오잉?  
![]({{site.baseurl}}/images/230920/before.PNG)  

---
## 1. 개발자도구로 html에서 확인
![]({{site.baseurl}}/images/230920/2.png)  
### html 내용 확인
1. 개발자도구(f12) 열고, Ctrl+Shift+C 혹은 왼쪽상단 버튼 누르기
2. 표 클릭   

-> 표 id같은게 있는지 확인~ (난 없음) 

---

## 2. 프로젝트에서 div id 검색해서, css 파일에 set 해주기
div id인 c-wrap-content 에다가 table 설정 내용을 넣어주면 됨~
````
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
표 스타일 CSS - border-collapse / border-spacing - [https://mine002.tistory.com/160](https://mine002.tistory.com/160)

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