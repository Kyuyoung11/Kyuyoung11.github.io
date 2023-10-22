---
layout: post
title: "[Spring] 스프링 핵심 원리 - 기본편 (2) 예제 만들기 "
categories: 
  - Java
  - Spring

tags: [Spring, 인프런]

toc: true
toc_sticky : true

date: 2023-10-22
last_modified_at: 2023-10-22
---


---
## 섹션 2. 스프링 핵심 원리 이해1 - 예제 만들기 

주문 도메인을 스프링 없이 구현하고, 나중에 스프링을 적용해보면서 핵심 원리에 대해 이해해보겠다.

---
### 비즈니스 요구사항과 설계
#### 요구사항
![]({{site.baseurl}}/images/4/2.PNG)

<br />

#### 설계
![]({{site.baseurl}}/images/4/1.PNG)

- 다형성이 잘 적용 되었다면, 정액할인정책에서 정률할인정책으로 바꿀 때 갈아끼워주기만 하면 된다.

---
### 생각해봐야 할 점

#### 아래 코드가 OCP 및 DIP를 잘 지키고 있을까?
- OCP (개방-폐쇄 원칙) - 다형성을 잘 지키는지
- DIP (의존관계 역전 원칙) - 클라이언트가 인터페이스에 의존해야 한다.

````java
public class OrderServiceImpl implements OrderService {
    private final MemberRepository memberRepository = new MemoryMemberRepository();
    ...
}
````

-> OrderService에서 MemberRepository를 가져올 때, 인터페이스(추상화)와 구현체 모두 의존하고 있음