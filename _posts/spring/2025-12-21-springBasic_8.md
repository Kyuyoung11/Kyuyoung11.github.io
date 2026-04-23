---
layout: post
title: "[Spring] 스프링 핵심 원리 - 기본편 (9) 빈 생명주기 콜백"
categories: 
  - Java
  - Spring

tags: [Spring, 인프런]

toc: true
toc_sticky : true

date: 2025-12-21
last_modified_at: 2025-12-21
---

## 섹션 9. 빈 생명주기 콜백


---
### 빈 생명주기 콜백 시작
#### 스프링 빈의 이벤트 라이프사이클
- 스프링 컨테이너 생성 -> 스프링 빈 생성 -> 의존관계 주입 -> 초기화 콜백 -> 사용 -> 소멸전 콜백 -> 스프링 종료
- 초기화 콜백 : 빈이 생성되고, 빈의 의존관계 주입이 완료된 후 호출
- 소멸전 콜백 : 빈이 소멸되기 직전에 호출
- 객체의 생성과 초기화를 분리하는 것이 유지보수 관점에서 좋음(무거운 초기화 작업)

#### 스프링의 빈 생명주기 콜백 방법
- 인터페이스(InitializingBean, DisposableBean)
- 설정 정보에 초기화 메서드, 종료 메서드 지정
- @PostConstruct, @PreDestroy 애노테이션 지원

<br /><br />

---
### 인터페이스(InitializingBean, DisposableBean)

````java
    @Override
    public void destroy() throws Exception {
        System.out.println("NetworkClient.destory");
        disconnect();
    }

    @Override
    public void afterPropertiesSet() throws Exception {
        connect();
        call("초기화 연결 메시지");
    }
````

#### 단점
- 스프링 전용 인터페이스
- 초기화, 소멸 메서드의 이름을 변경할 수 없다 (implements 해야하니까)
- 내가 코드를 고칠 수 없는 외부 라이브러리에 적용 불가능
- 초창기에 쓰던 방법이고 현재는 잘 사용하지 않음


<br /><br />

---
### 빈 등록 초기화, 소멸 메서드 지정
````java
        @Bean(initMethod = "init", destroyMethod = "close")
        public NetworkClient networkClient() {
            NetworkClient networkClient = new NetworkClient();
            networkClient.setUrl("http://hello-spring.dev");
            return networkClient;
        }
````

#### 장점
- 메서드 이름 자유롭게 줄 수 있음
- 스프링 코드에 의존하지 않음
- 외부 라이브러리에도 초기화, 종료 메서드 적용할 수 있음

#### ``@Bean(destroyMethod="")``에 특별한 기능이 있음
- 라이브러리는 대부분 close, shutdown 이라는 이름의 종료 메서드를 사용함 -> 기본값이 ``(inferred)`` 로 등록되어 알아서 추론해줌



---
### 애노테이션 @PostConstruct, @PreDestroy (이거 사용하면 됨)
````java
    @PreDestroy
    public void close(){
        System.out.println("NetworkClient.close");
        disconnect();
    }

    @PostConstruct
    public void init() {
        System.out.println("NetworkClient.init");
        connect();
        call("초기화 연결 메시지");
    }
````
#### 장점
- 최신 스프링에서 가장 권장하는 방법
- 스프링 종속적 기술이 아닌 JSR-250라는 자바 표준이다
- 컴포넌트 스캔과도 잘 어울림

#### 단점
- 외부 라이브러리에는 적용하지 못함


---
### 정리
- ``@PostConstruct, @PreDestory`` 애노테이션을 사용하자"
- 코드를 고칠 수 없는 외부 라이브러리를 초기화해야하면 @Bean의 ``initMethod``와 ``destroyMethod`` 사용하자