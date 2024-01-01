---
layout: post
title: "[Spring] 스프링 핵심 원리 - 기본편 (4) 스프링 컨테이너와 스프링 빈 "
categories: 
  - Java
  - Spring

tags: [Spring, 인프런]

toc: true
toc_sticky : true

date: 2023-12-31
last_modified_at: 2023-12-31
---

## 섹션 4. 스프링 컨테이너와 스프링 빈

강의 내용 : 지난 강의에서 구현한 주문 도메인에 스프링 적용

---
### 스프링 컨테이너
#### 스프링 컨테이너 생성
- `ApplicationContext` -> 스프링 컨테이너
- 스프링 컨테이너 안에 스프링 빈 저장소가 있음
- AppConfig.class 안에 빈을 등록하면 됨 (빈 이름은 유일해야 함)
- 빈에 의존관계를 설정하면 됨

---
### 스프링 빈
#### 스프링 빈 조회 - 기본
- `ac.getBean(빈이름, 타입)`
- `ac.getBean(타입)`
- `ac.getBeans(타입)`

#### 스프링 빈 조회 - 상속관계
- 부모 타입으로 조회하면 자식 타입도 함께 조회된다.

---
### BeanFactory와 ApplicationContext
![]({{site.baseurl}}/images/4/5.PNG)
#### BeanFactory
- 스프링 컨테이너의 최상위 인터페이스
- 지금까지 사용했던 대부분의 기능들이 BeanFactory에서 제공하는 기능들이다.

![]({{site.baseurl}}/images/4/6.PNG)
#### ApplicationContext
- BeanFactory 기능을 모두 상속받아서 제공
- 부가기능을 더 제공 함

`BeanFactory나 ApplicationContext를 스프링 컨테이너라 한다.`

---
### 다양한 설정 형식 지원 - 자바 코드, XML
- 장점 : 컴파일 없이 빈 설정 정보를 변경할 수 있다.
- xml 기반 설정은 최근엔 잘 사용하지 않음

---
### 스프링 빈 설정 메타 정보 - BeanDefinition
- `BeanDefinition` -> 추상화, 스프링이 다양한 설정 형식을 지원하는 이유
- 이 자체가 역할과 구현을 나눈 것이다
- 실무에서 직접 정의할 일은 거의 없다.
- 추상화해서 사용한다는 것이 중요!