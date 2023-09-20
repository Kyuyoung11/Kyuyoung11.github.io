---
layout: post
title: "[Spring] 스프링 핵심 원리 - 기본편 (1) - 객체 지향 설계와 스프링"
categories: Spring
tags: [Spring, 인프런]

toc: true
toc_sticky : true

date: 2023-09-17
last_modified_at: 2023-09-20
---

요즘 잘 모르고 개발하고 있나 라는 생각이 점점 들어서 강의를 들어보기로 했다.  
좀 더 실무에 맞게 스프링을 어떻게 사용하는지 이해할 수 있었으면...

---
## 섹션 1. 객체 지향 설계와 스프링

---
### (1) 이야기 - 자바 진영의 추운 겨울과 스프링의 탄생
#### 자바 ORM, JPA

- EJB -> (POJO) -> 스프링
- EJB 엔티티빈 -> 하이버네이트 -> JPA(자바표준)  

<br/>

#### 스프링 역사

- Rod Johnson의 책에 있는 예제 코드를 바탕으로 만들어짐  
<br/> 

스프링을 왜 이렇게 많이 쓸까?에 대해서 실습을 통해 알아가게 될 것이다...

---
### (2) 스프링이란?

`: 여러가지 기술들의 모음 `  
[https://spring.io/projects](https://spring.io/projects)  
- 스프링 프레임워크 : 가장 중요함. 핵심기술!
- 스프링 부트 : 스프링을 편리하게 사용할 수 있도록 지원

<br/>

#### 스프링 프레임워크 특징
- DI 컨테이너, AOP, 이벤트 등등.... 스프링 라이브러리를 이용해서 핵심 기술 제공

<br/>

#### 스프링 부트 특징
- 웹서버를 내장
- 쉬운 빌드
- 라이브러리 자동 구성
- 편한 설정

<br/>

#### 스프링의 핵심 개념/컨셉
- 자바 언어 기반 프레임워크 -> 객체 지향 언어  
  -> 스프링은 좋은 객체 지향 애플리케이션을 개발할 수 있게 도와주는 프레임워크 (그게 DI 컨테이너)

<br/>
좋은 객체 지향이 뭔지 알아야 스프링의 본질을 더 이해하기 쉬울 것이다.


----
### (3) 좋은 객체 지향 프로그래밍이란?
#### 객체 지향 프로그래밍? 
  - 객체들의 모임, 객체끼리 협력한다.
  - 유연&변경 용이 => 다형성

<br/>

#### 다형성
- 클라이언트에 영향을 주지않고, 새로운 기능 제공 가능
- 클라이언트가 내부 구조를 몰라도, 역할과 구현이 정해져있으면 대체 가능
- 예시
  - 운전자-자동차
  - 공연 무대   

-> 역할(인터페이스)과 구현(구현 클래스, 객체)을 분리해야, 유연하고 변경이 용이해진다. 

결론 : 인터페이스를 안정적으로 설계하는 것이 중요하다 ! (변화가 없도록~)

<br/>

#### 스프링과 객체 지향
- 객체 지향은 다형성이 정말 중요
- 제어의 역전(IoC), 의존관계 주입(DI) -> 다형성을 활용하여 역할과 구현을 편리하게 다룰 수 있게 지원하는 거임