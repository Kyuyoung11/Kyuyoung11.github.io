---
layout: post
title: "[Spring] 스프링 핵심 원리 - 기본편 (10) 빈 스코프"
categories: 
  - Java
  - Spring

tags: [Spring, 인프런]

toc: true
toc_sticky : true

date: 2025-12-26
last_modified_at: 2025-12-26
---

## 섹션 10. 빈 스코프

---
### 빈 스코프란?
#### 스프링이 지원하는 스코프
- **싱글톤** : 기본 스코프, 스프링 컨테이너의 시작과 종료까지 유지
- **프로토타입** : 프로토타입 빈의 생성과 의존관계 주입까지만 관여
- 웹 관련 스코프 
  - **request**
  - session
  - application

<br /><br />

---
### 프로토타입 스코프
#### 싱글톤 빈 요청
- 스프링 컨테이너는 본인이 관리하는 스프링 빈을 반환하고, 이후에 같은 요청이 와도 같은 객체 인스턴스의 스프링 빈을 반환함

#### 프로토타입 빈 요청
- 스프링 컨테이너는 빈 요청 시점에 프로토타입 빈을 생성하고, 필요한 의존관계를 주입한다.
- 생성한 프로토타입 빈을 클라이언트에 반환함 -> 스프링 컨테이너는 생성된 프로토타입 빈을 관리하지 않아서, @PreDestroy 같은 종료 메서드가 호출되지 않는다.

````
find prototypeBean1
PrototypeBean.init
find prototypeBean2
PrototypeBean.init
prototype1 = hello.core.scope.PrototypeTest$PrototypeBean@4149c063
prototype2 = hello.core.scope.PrototypeTest$PrototypeBean@9cb8225

Process finished with exit code 0

````
- destroy 실행 안됨 확인
- 스프링 컨테이너에 요청할 때마다 새로 생성

<br /><br />
---
### 프로토타입 스코프 - 싱글톤 빈과 함께 사용시 문제점

````java
    @Test
    void singletonClientUsePrototype() {
        AnnotationConfigApplicationContext ac = new AnnotationConfigApplicationContext(ClientBean.class, PrototypeBean.class);

        ClientBean clientBean1 = ac.getBean(ClientBean.class);
        int count1 = clientBean1.logic();
        assertThat(count1).isEqualTo(1);

        ClientBean clientBean2 = ac.getBean(ClientBean.class);
        int count2 = clientBean2.logic();
        assertThat(count2).isEqualTo(2);
    }
        
    @Scope("singleton")
    static class ClientBean {
        private final PrototypeBean prototypeBean;

        @Autowired
        public ClientBean(PrototypeBean prototypeBean) {
            this.prototypeBean = prototypeBean;
        }

        public int logic() {
            prototypeBean.addCount();
            return prototypeBean.getCount();
        }
    }
````
- 프로토타입 빈이 새로 생성되기는 하지만, 싱글톤 빈과 함께 유지됨
