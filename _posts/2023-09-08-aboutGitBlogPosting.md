---
layout: post
title: "[Jekyll] 깃 블로그 포스팅 방법"
categories: Jekyll
tags: [Blog, Git, Posting]

toc: true
toc_sticky : true

date: 2023-09-08
last_modified_at: 2023-09-08
---


포스팅 테스트도 할 겸... 포스팅 하는 방법을 써본다.  
사용중인 테마는 [flexton](http://jekyllthemes.org/themes/flexton/) 이다.

---
## 1. _posts 폴더에 Markdown 파일 생성

파일명 형식 : yyyy-mm-dd-title.md

---
## 2. 머릿말 작성 


```` text
--- 
layout: post
title: "깃 블로그 포스팅 방법"
categories: Jekyll
tags: [Blog, Git, Posting]

toc: true
toc_sticky : true

date: 2023-09-08
last_modified_at: 2023-09-12
---
````
toc(Table of Contents)은 목차 표시 기능이다.  
마크다운에서 #으로 구분해놓은걸 정리해서 알아서 띄워주는듯

toc_sticky를 true로 하면, 목차가 스크롤을 따라 움직인다.  
toc_icon, toc_label 설정까지 하면 커스터마이징도 가능한듯 (다음에 해봐야겠다)



---
## 참고 사이트
[Github 블로그] 블로그 포스팅하는 방법 - [https://ansohxxn.github.io/blog/posting/](https://ansohxxn.github.io/blog/posting/)  
마크다운 사용법 with velog - [https://velog.io/@wkdgus7113/Markdown-사용법](https://velog.io/@wkdgus7113/Markdown-사용법)   
TOC 사용 방법 - [https://devinlife.com/howto%20github%20pages/toc-table/](https://devinlife.com/howto%20github%20pages/toc-table/)
