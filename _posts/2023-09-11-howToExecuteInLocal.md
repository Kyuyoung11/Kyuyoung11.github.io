---
layout: post
title: "[Jekyll] 깃 블로그 로컬로 돌리기"
categories: Jekyll
tags: [Blog, Git, Local]

toc: true
toc_sticky : true

date: 2023-09-11
last_modified_at: 2023-09-12
---

하다보니 쓸데없는 푸쉬가 많아져서 안되겠음

---
## 1. Ruby 설치
https://rubyinstaller.org/downloads/

---
## 2. Jekyll 설치
```` shell
$ gem install bundler jekyll
````

--- 
## 3. $ bundle install  
````shell
$ bundle install 
````
-> 아래 오류난다. 'untaint' 뭘까.....
```` text
 [오류메시지]
 undefined method `untaint' for "C:/workspace/gitblog/flexton-master":String (NoMethodError)
 current  = File.expand_path(SharedHelpers.pwd).untaint
````
<br/>
해결은 이렇게 했음 (ruby 3.0.0부터 webrick이 빠졌다함)
````
$ bundle add webrick
````
다시 bundle install 안되면 bundle update

<br/>  


그 외에 확인해본 내용 
* Gemfile.lock에 적혀있는 번들 버전 -> 다시받고싶으면 아래와 같이 치면 됨
```` shell
$ gem cleanup
$ gem install bundler
````

---
## 4.실행
```` shell
$ bundle exec jekyll serve
````

---
## 5. http://127.0.0.1:4000/
들어가서 확인



---
## 참고 사이트  
[Github 블로그] github blog local에서 실행하기 (Windows) - [https://myung-ho.tistory.com/89](https://myung-ho.tistory.com/89)  
jekyll 테마 적용시킨 Github 블로그 로컬에서 변경사항 확인하기 - [https://dana3711.tistory.com/67](https://dana3711.tistory.com/67)