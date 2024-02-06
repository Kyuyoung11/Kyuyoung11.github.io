---
layout: post
title: "[Spring] 스프링 핵심 원리 - 기본편 (5) 싱글톤 컨테이너 "
categories: 
  - Java
  - Spring

tags: [Spring, 인프런]

toc: true
toc_sticky : true

date: 2024-02-04
last_modified_at: 2024-02-04
---

## 섹션 5. 싱글톤 컨테이너

강의 내용 : 지난 강의에서 구현한 주문 도메인에 스프링 적용

---
### 웹 애플리케이션과 싱글톤
스프링이 없는 순수한 DI -> 요청할때마다 생성하여야 함
- 메모리 낭비가 심하다
- 해결방안 : 객체를 1개만 생성하고 공유하도록 설계 ==> `싱글톤 패턴`

<br/>

### 싱글톤 패턴
`클래스의 인스턴스가 딱 1개만 생성하는 것을 보장하는 디자인 패턴`

코드
```
public class SingletonService {
    private static final SingletonService instance = new SingletonService();

    // 인스턴스를 이 메소드를 통해서만 조회할 수 있다.
    public static SingletonService getInstance() {
        return instance;
    }

    // 생성자를 private으로 선언해서 외부에서 new 키워드를 사용한 객체 생성을 못하게 막는다.
    private SingletonService() {
    }

    public void logic() {
        System.out.println("싱글톤 객체 로직 호출");
    }
}
```

싱글톤 패턴의 문제점
- 싱글톤 패턴을 구현하는 코드를 넣어야함
- 의존관계상 클라이언트가 구체 클래스에 의존한다 -> DIP 위반 (추상화에 의존해야함)
  - 구체클래스.getInstance() << 이 부분
- private 생성자로 만들어서 자식 클래스를 만들기 어려움

<br />

---
### 싱글톤 컨테이너
스프링 컨테이너는 싱글톤 패턴의 문제점을 해결하면서, 싱글톤 패턴을 적용하지 않아도 객체 인스턴스를 싱글톤으로 관리함.
- 스프링 빈
- 고객의 요청이 올 때마다 객체를 생성하는 것이 아니라, 만들어진 객체를 공유해서 효율적으로 재사용
  - (참고 : 요청할 때마다 새로운 객체를 생성하는 기능도 제공함)

<br />

### 싱글톤 방식의 주의점
- 여러 클라이언트가 하나의 같은 객체 인스턴스를 공유함 => 상태를 유지하게 설계하면 안된다.
- 무상태(stateless) 설계
  - 특정 클라이언트에 의존적인 필드가 있으면 안됨
  - 값을 변경할 수 있는 필드가 있으면 안됨
  - 가급적 읽기만!
