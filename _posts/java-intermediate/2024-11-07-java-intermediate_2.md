---
layout: post
title: "[김영한의 실전 자바] 중급 1편 - 불변 객체"
categories: 
  - Java
  - Intermediate

tags: [자바 중급, 인프런]

toc: true
toc_sticky : true

date: 2024-11-07
last_modified_at: 2024-11-07
---


---
## 기본형과 참조형의 공유
### 기본형(Primitive Type)
- 하나의 값을 여러 변수에서 절대로 공유하지 않는다.
  - ````java
        //기본형은 절대로 같은 값을 공유하지 않는다.
        int a = 10;
        int b = a; // a-> 값 복사
        System.out.println("a = " + a); // 10
        System.out.println("b = " + b); // 10

        b = 20;
        System.out.println("20 -> b");
        System.out.println("a = " + a); // 10
        System.out.println("b = " + b); // 20
    ````
    - ``b = a`` 라고 하면 자바는 항상 값을 복사해서 대입함 

<br>

### 참조형(Reference Type) 
- 하나의 객체를 참조값을 통해 여러 변수에서 공유할 수 있다.
  - ````java
        //참조형 변수는 하나의 인스턴스를 공유할 수 있다.
        Address a = new Address("서울");
        Address b = a;

        System.out.println("a = " + a); // 서울
        System.out.println("b = " + b); // 서울

        b.setValue("부산");
        System.out.println("부산 -> b");
        System.out.println("a = " + a); // 부산
        System.out.println("b = " + b); // 부산
    ````

<br> <br>

----
## 공유 참조와 사이드 이펙트
- 위에서 ``a = 부산`` 으로 나오게 된게 사이드 이펙트임

````java
        Address a = new Address("서울"); // x001
        Address b = new Address("서울"); // x002
````
- 객체 생성을 따로 해서 아예 주소를 분리하면 해결할 수 있다.
- **여러 변수가 하나의 객체를 공유하는 것을 막을 방법은 없다.**
  - 그냥 생성부터 다른 객체를 참조하면 됨!

<br><br>

----
## 불변 객체 - 도입
- 앞선 문제들의 원인은 객체를 여러 변수에서 공유했기 때문이다.
  - 정확히는 공유된 객체의 값을 변경한 것에 있다!

<br> 

### 불변 객체 도입
- 불변 객체(Immutable Object) : 객체의 상태(값, 필드, 멤버 변수)가 변하지 않는 객체
- 불변 클래스
  - ````java
    public class ImmutableAddress {

      private final String value;
  
      public ImmutableAddress(String value) {
          this.value = value;
      }
  
      public String getValue() {
          return value;
      }
  
      @Override
      public String toString() {
          return "Address{" +
                  "value='" + value + '\'' +
                  '}';
      }

    }
    ````
  - 필드를 ``final``로 선언
  - setter 를 사용할 수 없음

### 정리
- 불변이라는 단순한 제약을 사용해서 사이드 이펙트를 막을 수 있다.


---
## 불변 객체 - 값 변경

**값 변경**

````java
    public static void main(String[] args) {
        MutableObj obj = new MutableObj(10);

        obj.add(20);

        //계산 이후엔 기존 값이 사라짐
        System.out.println(obj);
    }
````

````java
    public void add(int addValue) {
        value+= addValue;
    }
````
- 불변 객체 아닐땐 보통 이렇게 값 변경 할거임

<br>

````java
    public ImmutableObj add(int addValue) {

        return new ImmutableObj(value + addValue);
    }
````
- 이렇게 하면 새로운 객체를 반환하여 불변객체의 값을 변경할 수 있음

<br><br>

*[참고] 불변객체를 반환하여 값 변경하고자 할 때 method ``with~~`` 로 하는게 관례임*

<br><br>

---
## 정리
- 자바가 기본으로 제공하는 ``Integer``, ``LocalDate`` 같은 클래스들이 불변으로 설계되어 있다.
- 이 외 장점들 : 캐시 안정성, 멀티 쓰레드 안정성, 엔티티 값 타입
- 모든 클래스를 불변으로 만드는 것은 아니다! (값을 변경하면 안되는 특별한 경우에 만들어서 사용)
