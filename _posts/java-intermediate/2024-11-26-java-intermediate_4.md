---
layout: post
title: "[김영한의 실전 자바] 중급 1편 - 래퍼 클래스"
categories: 
  - Java
  - Intermediate

tags: [자바 중급, 인프런]

toc: true
toc_sticky : true

date: 2025-07-17
last_modified_at: 2025-07-17
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

<br><br><br>

---
## 오토 박싱
- 박싱 : valueOf()
- 언박싱 : xxxValue()
<br>
-> 개발자가 변환을 자주 사용함에 따라 자바 1.5부터 오토박싱/언박싱을 지원함
```java
    int value = 7;
    Integer boxedValue = Integer.valueOf(value); // 박싱
    Integer boxedValue = value; // 오토 박싱
    
    int unboxedValue = boxedValue.intValue(); // 언박싱
    int unboxedValue = boxedValue; // 오토 언박싱
```
- 오토 박싱/언박싱 : 컴파일러가 개발자 대신 ``valueOf``, ``xxxValue()``등의 코드를 추가해주는 기능

<br><br><br>

---
## 주요 메서드와 성능
````java
    Integer i1 = Integer.valueOf(10); // 숫자를 래퍼 객체로 변환
    Integer.valueOf("10"); // 문자열을 래퍼 객체로 변환
    int intVLaue = Integer.parseInt("10"); // 문자열 전용, 기본형 변환


    // 비교
    int compareResult = i1.compareTo(20);
    System.out.println("compareResult = " + compareResult);

    //산술 연산
    System.out.println("sum : " + Integer.sum(10,20));
    System.out.println("min : " + Integer.min(10,20));
    System.out.println("max : " + Integer.max(10,20));
````
### parseInt() vs valueOf()
- valueOf -> 래퍼타입 반환
- parseInt -> 기본형 반환

<br>

### 래퍼 클래스와 성능
- 다양한 기능을 제공하는 래퍼 클래스가 있음에도 기본형을 사용하는 이유?
  - 기본형이 더 빠름
- 기본형이 더 성능이 좋은 이유
  - 기본형은 메모리에서 단순히 그 크기만큼의 공간을 차지함 (ex. int는 4바이트)
  - 래퍼 클래스의 인스턴스는 내부에 필드로 가지고 있는 값뿐만 아니라 객체 메타데이터를 포함함 (8~16바이트 사용)
- 기본형과 래퍼 클래스 어떤 것을 사용해야할까?
  - 1회 수행 기준으로는 사실 성능을 고려해야 할 만큼의 차이는 나지 않음
  - CPU 연산을 많이 수행하는 경우에는 **기본형**을 사용해서 최적화하는 것이 좋음
  - 일반적인 경우에는 **코드를 유지보수**하기 더 나은 쪽으로 선택

<br>

### 유지보수 vs 최적화
- 유지보수하기 좋은 코드를 먼저 고민해야 한다. (최신 컴퓨터는 성능이 좋기 때문에...)
- 성능 최적화는 대부분 단순화보다 복잡함을 요구하고, 더 많은 코드들을 추가로 만들어야 한다.
- 웹 어플리케이션에서는 연산보다 네트워크 호출이 수십만배는 더 오래걸림 -> 차라리 네트워크 호출 한 번을 줄이자
- 결론 : 개발 이후에 성능 테스트를 해보고 정말 문제가 되는 부분을 최적화 한다.


<br><br><br>

---
## Class 클래스
### 리플렉션 - reflection
- Class 를 사용하면 메소드, 필드, 생성자 등을 조회하고 이들을 통해 객체 인스턴스를 생성하거나 메소드를 호출하는 작업을 할 수 있다. 이런 작업을 리플렉션이라 한다.


<br><br><br>
