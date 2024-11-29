---
layout: post
title: "[김영한의 실전 자바] 중급 1편 - 래퍼 클래스"
categories: 
  - Java
  - Intermediate

tags: [자바 중급, 인프런]

toc: true
toc_sticky : true

date: 2024-11-26
last_modified_at: 2024-11-26
---


---
## 기본형의 한계 
- 기본형 데이터는 객체가 아님 => 객체 지향 프로그래밍의 장점을 살릴 수 없음. (ex. 메서드 제공)
- null 값을 가질 수 없음

<br>

### 직접 만든 래퍼 클래스
- 래퍼 클래스(Wrapper class) : 특정 기본형을 감싸서 만드는 클래스
- 객체를 만들어서 메소드만 호출해보면 훨씬 편리한 걸 알 수 있음.

<br><br><br>

---
## 자바 래퍼 클래스
- 자바는 기본형에 대응하는 래퍼 클래스를 기본으로 제공한다
  - int -> Integer / boolean -> Boolean 이런 식
- 특징 : 불변이다, ``equals``로 비교해야 한다.

<br>

### 박싱 (Boxing)
- 기본형을 래퍼 클래스로 변경하는 것 
- ``new Integer(10)`` 이건 삭제 예정이라, ``Integer.valueOf(10)`` 이걸로 사용하도록 함
- ``.intValue()`` -> 언박싱 
- 객체이기 때문에, 값 비교하려면 ``.equals()`` 사용해야 함.