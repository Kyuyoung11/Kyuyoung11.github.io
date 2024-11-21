---
layout: post
title: "[김영한의 실전 자바] 중급 1편 - String 클래스"
categories: 
  - Java
  - Intermediate

tags: [자바 중급, 인프런]

toc: true
toc_sticky : true

date: 2024-11-19
last_modified_at: 2024-11-19
---


---
## String 클래스 - 기본
- ``char`` - 문자 하나를 다룰 때 사용
- ``char[]`` - char를 사용해서 여러 문자를 나열
- ``String`` - char[]로 문자를 나열하는 건 불편하니 String이 있는 것
  - 대문자로 시작하는 이유도 이런 것... ``참조형``임!

<br>

````java
public final class String {
    
    //문자열 보관
  private final char[] value; // 자바 9 이전
  private final byte[] value; // 자바 9 이후
}
````
- 이런 필드로 구성되어 있다.
<br><br>
````java
    public static void main(String[] args) {
        String a = "hello";
        String b = " java";

        String result = a.concat(b);
        String result2 = a + b;

        System.out.println(result);
        System.out.println(result2);
    }
````
- 여기서 어떻게 ``+`` 연산으로 concat 기능을 쓸 수 있을까?
  - 자주 다루어지는거라 특별히 편의상 ``+`` 연산을 제공하는거임~ 그냥 되는게 아님!

<br><br><br><br>

---
## String 클래스 - 불변 객체
- String은 불변으로 설계됨
- 왜?
  - String은 문자열 풀을 통해 최적화를 함. <br>
    이 문자열 풀에서 특정 문자를 수정하면, 같은 문자를 참조하는 변수의 모든 문자가 함께 변경되는 문제가 있음.


---
## String 클래스 - 가변 String
- 불변인 String 클래스의 단점
  - 문자를 더하거나 변경할 때마다 계속해서 새로운 객체를 생성해야함 -> 컴퓨터 자원 소모

<br>

**StringBuilder**
- 위 문제를 해결하는 단순한 방법! 가변 ``String``이 존재하면 됨~
- 다 쓰고 ``.toString()`` 으로 불변으로 사용해야 좋음~ 그래야 사이드 이펙트가 발생하지 않음


<br><br><br>

---
## String 최적화
1. 문자열 리터럴 최적화 
   - ````java
     String helloWorld = "Hello, " + "World!"; //컴파일 전
     
     String helloWorld = "Hello, World!"; // 컴파일 후
     ````
   - 알아서 합쳐놓음
2. String 변수 최적화
   - ``+`` 연산 사용하면, 안에서 알아서 StringBuilder, append로 수행함
   - StringBuilder를 직접 사용하는 것이 더 좋은 경우
     - 반복문에서 반복해서 문자 연결할 때 (+ 연산은 결국 계속 String 객체를 생성해야 하기 때문에)
     - 복잡한 문자열의 특정 부분을 변경해야 할 때
     - 매우 긴 대용량 문자열을 다룰 때

<br>

**(참고)``StringBuffer``는 무엇인가?**
- StringBuilder와 똑같은 기능을 수행함 
- 내부에 동기화가 있어서, 멀티 스레드 상황에서 안전 / 동기화 오버헤드로 성능은 느림

<br><br><br>

---
## 메서드 체이닝
````java
public class ValueAdder {
    private int value;

    public ValueAdder add(int addValue) {
        value += addValue;
        return this;
    }

    public int getValue() {
        return value;
    }
}

public class MethodChainingMain1 {
  public static void main(String[] args) {
    ValueAdder adder = new ValueAdder();

    System.out.println("result = " + adder.add(1).add(2).add(3).getValue()); // 6
  }
}
````
- 이러면 메서드 호출 결과로 **자기 자신의 참조값**을 반환받음 -> 메서드 호출을 계속 이어갈 수 있음
- 장점 : 코드를 간결하고 가독성을 높여줌
- ``StringBuilder``도 이렇게 ``.append('a').append('b')...`` 연결해서 쓸 수 있음