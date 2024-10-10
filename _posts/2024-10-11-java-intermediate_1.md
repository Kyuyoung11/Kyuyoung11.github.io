---
layout: post
title: "[김영한의 실전 자바] 중급 1편 - Object 클래스"
categories: 
  - Java
  - Intermediate

tags: [자바 중급, 인프런]

toc: true
toc_sticky : true

date: 2024-10-11
last_modified_at: 2024-10-11
---

자바의 기능들을 본질적으로 왜 쓰는지 이해하고 활용하기 위해서 듣겠다


---
## java.lang 패키지 소개

<br />

**java.lang 패키지의 대표적 클래스들**
- Object : 모든 자바 객체의 부모 클래스
- String : 문자열
- Integer, Long, Double : 래퍼 타입, 기본형 데이터 타입을 객체로 만든 것
- Class : 클래스 메타 정보
- System : 시스템과 관련된 기본 기능들을 제공

-> 이건 자바 언어의 기본을 이루는거임 (import 생략이 가능하다)

<br /><br /><br />

---
## Object 클래스
자바에서 모든 클래스의 최상위 부모클래스는 ``Object`` 클래스이다.

<br />

````java
public class Parent {

    public void parentMethod() {
        System.out.println("Parent.parentMethod");
    }
}
````
- 부모 클래스가 없으면 묵시적으로 Object 클래스를 상속받는다.
  - ``public class Parent extends Object {``한 것과 같음

<br /><br />


**child.toString() 메서드를 호출하였을 때 실행 결과**
1. ``Child``에서 ``toString()``을 찾음 
2. 없으면 부모 타입인 ``Parent``에서 찾음
3. 없으면 부모 타입인 ``Object``에서 찾음 (``Object``에는 ``toString()``이 있음!)
4. 있으면 호출~

<br /><br />

**자바에서 Object 클래스가 최상위 부모 클래스인 이유**
- 공통 기능 제공 -> 일관성을 가짐
- 다형성의 기본 구현

<br /><br />


