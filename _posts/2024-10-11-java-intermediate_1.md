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

---
## Object 다형성

**Object 다형성의 한계**
````java
public class ObjectPolyExample1 {

    public static void main(String[] args) {
        Dog dog = new Dog();
        Car car = new Car();

        action(dog);
        action(car);
    }


    private static void action(Object obj) {

        //컴파일 오류
//        obj.sound(); //Object는 sound()가 없다.
//        obj.move(); // Object는 move()가 없다.

        //호출하는 방법 -> 객체에 맞는 다운캐스팅 필요
        if (obj instanceof Dog dog) {
            dog.sound();
        } else if (obj instanceof Car car) {
            car.move();
        }

    }
}

````
- ``obj.sound()``를 호출하면 Object에서 ``sound()``를 찾는다. 
-> 없으면 부모로 올라가는데, Object가 최종부모이니 올라갈 수 없음
-> 오류발생 

- 다운캐스팅을 하게되면 Dog 에서 ``sound()``를 찾아서 호출함.
- Object를 통해 전달 받은 객체를 호출하려면 다운캐스팅 과정이 필요한 한계가 있음
- 다형성을 제대로 참조하려면 다형적 참조 + 메서드 오버라이딩을 함께 사용해야함. 
  - Object에선 메서드 오버라이딩을 활용할 수 없음

---
## Object 배열

````java
public class ObjectPolyExample2 {
    public static void main(String[] args) {
        Dog dog = new Dog();
        Car car = new Car();
        Object object = new Object();

        Object[] objects = {dog, car, object};

        size(objects);
    }

    private static void size(Object[] objects) {
        System.out.println("전달된 객체의 수는: " + objects.length);
    }
}
````

- ``size()`` 메서드는 Object 타입만 사용하기 때문에, 자바를 쓰는 어떤 곳에서든 사용 가능함


---
## Object가 없다면?
- 모든 객체를 받을 수 있는 메서드를 만들 수 없음
- 모든 객체를 저장할 수 있는 배열을 만들 수 없음
- ``MyObject`` 같은 클래스를 직접 만들어서 쓸 수는 있지만, 모든 개발자가 만들어서 쓰는건 호환성이 떨어진다.


---
## toString()
- 객체의 정보를 문자열 형태로 제공함. 
- 디버깅과 로깅에서 유용하게 사용함

````java
    public String toString() {
        return getClass().getName() + "@" + Integer.toHexString(hashCode());
    }
````
- Object가 제공하는 ``toString()`` 메서드는 기본적으로 패키지를 포함한 객체의 이름과 참조값을 제공한다.


<br />

````java
public class ToStringMain1 {
    public static void main(String[] args) {
        Object object = new Object();
        String string = object.toString();

        //결과가 같게 나옴 - java.lang.Object@10f87f48
        System.out.println(string);
        System.out.println(object);
    }
}
````
- 어떻게 두개가 결과값이 똑같을까~
- ``println()`` -> 여기서 ``obj.toString()``을 호출하고있음

<br /> <br />


**toString() 오버라이딩**
- 보통 오버라이딩으로 재정의하여 유용한 정보를 제공함~

````java

public class ObjectPrinter {
  public static void print(Object obj) {
    String string = "객체 정보 출력: " + obj.toString();
    System.out.println(string);

  }
}


public class ToStringMain2 {
  public static void main(String[] args) {
    Car car = new Car("Model Y");

    Dog dog1 = new Dog("멍멍이1" , 2);
    Dog dog2 = new Dog("멍멍이2", 5);

    System.out.println("1. 단순 toString 호출");
    System.out.println(car.toString());
    System.out.println(dog1.toString());
    System.out.println(dog2.toString());

    System.out.println("2. println 내부에서 toString 호출");
    System.out.println(car);
    System.out.println(dog1);
    System.out.println(dog2);

    System.out.println("3. Object 다형성 활용");
    ObjectPrinter.print(car);
    ObjectPrinter.print(dog1);
    ObjectPrinter.print(dog2);


  }
}
````
- 이렇게 쓰는 것도 결과가 똑같이 나옴
- 인텔리제이에선 ``toString()`` 자동생성도 가능~

1. Object에서 ``toString()`` 을 찾음
2. 자식에 오버라이딩된 메서드가 있는지 찾아보고 있으면 자식에서 출력~

<br /> <br/>

**(참고) 객체의 참조값을 출력하는 방법**
````java
Integer.toHexString(System.identityHashCode(dog1));
````
- HashCode를 16진수로 변환하는거임

<br /><br /><br />

---
## equals()

### 1. 동일성과 동등성
- 동일성(Identity) : ``==``연산자를 사용해서 참조가 동일한 객체를 가리키는지 확인
- 동등성(Equality) : ``equals()`` 메서드를 사용하여 두 객체가 논리적으로 동등한지 확인

````java
        UserV1 userV1 = new UserV1("id-100");
        UserV1 userV2 = new UserV1("id-100");

        System.out.println("identity = " + (userV1 == userV2)); // false
        System.out.println("equality = " + (userV1.equals(userV2))); // false
````
- 둘 다 false임
  - Object에서 기본으로 제공하는 ``equals()`` 는 ``==``으로 동일성 비교를 제공함
  - ````java
      public boolean equals(Object obj) {
          return (this == obj);
      }
    ````

-> 동등성을 비교하고 싶으면 메서드를 재정의해서 사용해야한다.


<br /><br />

### 2. 구현
````java
    @Override
    public boolean equals(Object obj) {

        UserV2 user = (UserV2) obj;

        boolean result = id.equals((user.id));
        return result;

    }
````
- 이렇게 하고 다시 실행하면 equals 비교는 true임

<br />

**정확한 equals() 구현**
````java
    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;
        UserV2 userV2 = (UserV2) o;
        return Objects.equals(id, userV2.id);
    }
````
- equals() 메서드를 구현할 때 지켜야 하는 규칙 - 반사성, 대칭성, 추이성, 일관성, null에 대한 비교

<br /><br /><br />

---
## 정리

**Object의 나머지 메서드**
- ``clone()`` -> 객체를 복사
- ``hashCode()`` -> equals()와 hashCode()는 종종 함께 사용.
- ``getClass()`` -> Class 정보를 알 수 있음
- ``notify()`` ... -> 멀티스레드 관련 메서드