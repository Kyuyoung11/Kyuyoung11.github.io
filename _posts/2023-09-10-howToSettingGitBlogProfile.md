---
layout: post
title: "[GitBlog] 블꾸 (1) - 프로필, 폰트"
categories: 
  - GitBlog

tags: [Blog, Git, Profile, Jekyll]
toc: true
toc_sticky : true
date: 2023-09-10
last_modified_at: 2023-09-12

---

처음 가져온 [테마](http://jekyllthemes.org/themes/flexton/)에서 내 마음대로 설정하는 방법을 정리

---
## 1. 프로필 설정
바꾸고싶은 화면 소스를 보니, 어딘가에서 setting 하고 있는듯
```` html
home.html
    ...
    <div class="c-author__info">
      <div class="c-author__name">{{site.author-name}}</div>
      <span class="c-author__job">{{site.author-job}}</span>
    </div>
    ...
````

```` yml
_config.yml

# Author
author-name:    이름
author-image:   1.jpg   
author-job:     Developer
author-email:   your-email@domain.com # Add your email for contant form.
author-twitter: artemsheludko_ # Add your twitter account
about-author:   I am a web developer focusing on front-end development. Always hungry to keep learning.
````
갓챠 내 정보에 맞게 바꿔주면 끝

---
## 2. 폰트 설정

### (1) 구글폰트에서 폰트 고르기  
[https://fonts.google.com/?subset=korean](https://fonts.google.com/?subset=korean)


난 나눔고딕코딩 픽   
[https://fonts.google.com/specimen/Nanum+Gothic+Coding?query=coding](https://fonts.google.com/specimen/Nanum+Gothic+Coding?query=coding)

![]({{site.baseurl}}/images/230910/230911_1.PNG)
@import url 부분 복사

<br/>  

### (2) main.scss에 붙여넣기
```` css
@import url('https://fonts.googleapis.com/css2?family=Nanum+Gothic+Coding&display=swap');
````

<br/>  

### (3) 사용할 css 파일에 넣기
내가 쓰는 테마는 뭔가 변수같이 쓸 수 있게 해둔듯
```` css
_typography.scss

$base-font-family: "Nanum Gothic Coding", 'Open Sans', Helvetica Neue, Helvetica, Arial, sans-serif;
$heading-font-family: "Nanum Gothic Coding", 'Volkhov', 'Times New Roman', Times, serif;
````
앞에 넣어주면 된다 (쓴 순서대로 적용됨)

<br/>  

### (4) 확인

---
## 참고 사이트
[Github 블로그] 웹 폰트 설정하기 (+폰트 추천) - [https://ansohxxn.github.io/blog/font/](https://ansohxxn.github.io/blog/font/)

---

## 앞으로 하고싶은거
* 색 커스텀
* 전체적으로 폰트크기, 글자간격 조정
* 통계 페이지 추가
* 카테고리
* 목차

아... 할거많네