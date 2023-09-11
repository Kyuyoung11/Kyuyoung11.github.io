---
layout: post
title: "[Jekyll] 깃 블로그 프로필 꾸미기 (깃꾸~)"
tags: [Blog, Git, Profile]

toc: true
toc_sticky : true

date: 2023-09-10
last_modified_at: 2023-09-10
---

처음 가져온 [테마](http://jekyllthemes.org/themes/flexton/)에서 내 마음대로 설정하는 방법을 정리


## 1. 프로필 설정
___
바꾸고싶은 화면 소스를 보니, 어딘가에서 setting 하고 있는듯
````
home.html
    ...
    <div class="c-author__info">
      <div class="c-author__name">{{site.author-name}}</div>
      <span class="c-author__job">{{site.author-job}}</span>
    </div>
    ...
````

````
_config.yml

# Author
author-name:    규영
author-image:   1.jpg   
author-job:     Developer
author-email:   your-email@domain.com # Add your email for contant form.
author-twitter: artemsheludko_ # Add your twitter account
about-author:   I am a web developer focusing on front-end development. Always hungry to keep learning.
````
갓챠 내 정보에 맞게 바꿔주면 끝

---
## 2. 폰트 설정

(1) 구글폰트에서 폰트 고르기  
난 나눔고딕코딩 픽  
https://fonts.google.com/specimen/Nanum+Gothic+Coding?query=coding
![]({{site.baseurl}}/images/230910/230911_1.PNG)