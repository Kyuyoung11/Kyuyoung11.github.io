---
layout: post
title: "[GitBlog] 블꾸 (3) - 사이드바에 카테고리 추가하기"
categories: 
  - GitBlog

tags: [Blog, Git, Category, Sidebar, Navigation]
toc: true
toc_sticky : true
date: 2023-09-26
last_modified_at: 2023-09-26

---
너무 헤매면서 설정해서 그냥 애초에 카테고리가 있는 테마를 선택하길 
<br/>

참조 블로그 : [https://ansohxxn.github.io/blog/category/](https://ansohxxn.github.io/blog/category/)  
잘 정리되어 있음

minimal-mistake 테마에 작성된걸 내 테마에 이식하는.... 아주 멋진 작업이었다... 그래

---
## 1. _data/navigation.yml 추가 
_data 디렉토리 밑에 navigation.yml 파일을 추가한다. url 맞게 들어갔는지 확인
````yml
# main links
main:
  - title: "Home"
    url: /index.html
    #- title: "About"
    #url: /about/
  - title: "Category"
    url: /category/
    #- title: "Tag"
    #url: /tags/
    #- title: "Post by Year"
    #url: /year-archive/

````
---

## 2. _include/sidebar.html 추가
`````` html
{% raw %}
{% if page.author_profile or layout.author_profile or page.sidebar %}
<div class="sidebar sticky">
    {% if page.sidebar %}
    {% for s in page.sidebar %}
    {% if s.image %}
    <img src="{{ s.image | relative_url }}"
         alt="{% if s.image_alt %}{{ s.image_alt }}{% endif %}">
    {% endif %}
    {% if s.title %}<h3>{{ s.title }}</h3>{% endif %}
    {% if s.text %}{{ s.text | markdownify }}{% endif %}
    {% if s.nav %}{% include nav_list nav=s.nav %}{% endif %}
    {% endfor %}
    {% if page.sidebar.nav %}
    {% include nav_list nav=page.sidebar.nav %}
    {% endif %}
    {% endif %}

    {% if page.sidebar_main %}
    {% include nav_list_main %}
    {% endif %}

</div>
{% endif %}
{% endraw %}
``````
여기서 `{ include nav_list_main }` 코드를 통해 nav_list_main 파일을 불러온다.

---
## 3. _include/nav_list_main 파일 추가
````html
{% raw %}
 {% assign sum = site.posts | size %}
  <nav class="nav__list">
    <ul class="nav__items" id="category_tag_menu">
        <li>
              📂 <span style="">전체 글 수</style> <span style="">{{sum}}</style> <span style="">개</style>
        </li>
        <li>
          <span class="nav__sub-title">Java</span>
              <ul>
                  {% for category in site.categories %}
                      {% if category[0] == "Spring" %}
                          <li><a href="/category/spring/" class="">Spring ({{category[1].size}})</a></li>
                      {% endif %}
                  {% endfor %}
              </ul>
              <ul>
                  {% for category in site.categories %}
                      {% if category[0] == "TDD" %}
                          <li><a href="/category/tdd/" class="">TDD & Clean Code ({{category[1].size}})</a></li>
                      {% endif %}
                  {% endfor %}
              </ul>
        </li>
    </ul>
  </nav>
{% endraw %}
````
주의할 점
- `for category in site.categories`  
  `if category[0] == "Spring"`
  - post에서 categories 머릿말에 Spring로 썼는지 확인  

---
## 4. _pages/category/. 에 추가
````html
{% raw %}
---
title: "Spring"
layout: category-page
permalink: category/spring/
sidebar_main: true
---


{% assign posts = site.categories.spring %}
{% for post in posts %} {% include category-page.html type=page.entries_layout %} {% endfor %}
{% endraw %}
````

- title : post 머릿말 categories에 썼던 그대로 넣기
- layout : 카테고리 클릭했을 때, 불러올 html 파일 (layout 디렉토리 밑에 있어야 할 느낌)
- permalink : 카테고리 클릭했을 때, 연결될 link (nav_list_main에 쓴거랑 맞춰서 쓰기) 
- sidebar_main: true 를 하면 nav_list_main을 불러온다는~ 
- `include category-page.html type=page.entries_layout` 
  - category-page.html 파일이 카테고리 클릭 시, 표시될 html


---

## 앞으로 하고싶은거
* 글자간격 조정
* 통계 페이지 추가
* 아카이브 페이지 추가
* 목차



아 어렵다~