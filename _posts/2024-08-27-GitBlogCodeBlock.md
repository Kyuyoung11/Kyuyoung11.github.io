---
layout: post
title: "[GitBlog] 블꾸 (4) - 코드블록 디자인 넣기"
categories: 
  - GitBlog

tags: [Blog, Git, Gitio]
toc: true
toc_sticky : true
date: 2024-08-27
last_modified_at: 2024-08-27

---



---
참고한 블로그는 여기
- [https://mi2mic.tistory.com/179](https://mi2mic.tistory.com/179)
- [https://slothspeed.tistory.com/44](https://slothspeed.tistory.com/44)

---
## 1. 코드블럭 테마 넣기
### html 코드 넣기
아래 링크에서 Usage > HTML Tags 부분을 참고하면 된다.
- [https://highlightjs.org/](https://highlightjs.org/)
![]({{site.baseurl}}/images/4/240827_1.png)

<br/>

해당 내용을 \<head> ... \</head> 사이에 넣어주면 됨

````html
head.html

  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.9.0/styles/default.min.css">
  <script src="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.9.0/highlight.min.js"></script>

  <script>hljs.highlightAll();</script>
````

<br/><br/><br/>

### 테마 적용 
아래 링크에서 마음에 드는것으로 ``default.min.css`` 부분을 바꿔준다.
- [https://highlightjs.org/demo](https://highlightjs.org/demo)
- 난 ``atom-one-dark-reasonable.min.css`` 선택
  ![]({{site.baseurl}}/images/4/240827_2.png)

<br/><br/><br/>

---

## 2. 줄번호 생성
### html 코드 넣기
아래 링크에서 README를 참고
- [https://github.com/wcoder/highlightjs-line-numbers.js](https://github.com/wcoder/highlightjs-line-numbers.js)

<br/>

결론은 똑같이 \<head> ... \</head>에 아래 코드를 넣어주면 된다. 
````html
head.html

<script src="//cdnjs.cloudflare.com/ajax/libs/highlightjs-line-numbers.js/2.8.0/highlightjs-line-numbers.min.js"></script>
<script>hljs.initHighlightingOnLoad();</script>
````

<br/>

나는 이런 식으로 이상하게 줄이 생성되었다. 
![]({{site.baseurl}}/images/4/240827_3.png)

<br/>

개발자 도구를 열어서 어떤 scss가 적용된건지 확인한다.
![]({{site.baseurl}}/images/4/240827_4.png)

-> 나의 경우는 ``.c-wrap-content table`` 이었다. 이걸 ``.c-wrap-content > table`` 로 바꿔주면 됨

````scss
_article-page.scss

.c-wrap-content {
  padding: 20px;
  background-color: $white-color;
}

.c-wrap-content > table{

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


  thead {
    background-color: $sub-background;
    border-bottom: 2px solid mix(#000, $border-color-post, 25%);
  }
...

````

이런 식으로 바꿔주니 적용되었다.




