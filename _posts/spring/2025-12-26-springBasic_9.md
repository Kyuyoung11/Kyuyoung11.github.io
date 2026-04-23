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

<br />

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

<br /><br />

---
### 프로토타입 스코프 - 싱글톤 빈과 함께 사용시 Provider로 문제 해결
#### ObjectFactory, ObjectProvider
- ObjectProvider - 지정한 빈을 컨테이너에서 대신 찾아주는 DL 서비스를 제공, ObjectFactory 상속

````java
    @Test
    void singletonClientUsePrototype() {
        AnnotationConfigApplicationContext ac = new AnnotationConfigApplicationContext(ClientBean.class, PrototypeBean.class);

        ClientBean clientBean1 = ac.getBean(ClientBean.class);
        int count1 = clientBean1.logic();
        assertThat(count1).isEqualTo(1);

        ClientBean clientBean2 = ac.getBean(ClientBean.class);
        int count2 = clientBean2.logic();
        assertThat(count2).isEqualTo(1);
    }

    @Scope("singleton")
    static class ClientBean {

        @Autowired
        private ObjectProvider<PrototypeBean> prototypeBeanProvider;

        public int logic() {
            PrototypeBean prototypeBean = prototypeBeanProvider.getObject();
            prototypeBean.addCount();
            return prototypeBean.getCount();
        }
    }
````
- ``getObject()``을 통해서 항상 새로운 프로토타입 빈이 생성되는 것을 확인할 수 있음

<br />

#### JSR-330 Provider
- ``jakarta.inject:jakarta.inject-api:2.0.1`` 라이브러리 gradle 추가 후 사용

````java
    @Scope("singleton")
    static class ClientBean {
        @Autowired
        private Provider<PrototypeBean> prototypeBeanProvider;

        public int logic() {
            PrototypeBean prototypeBean = prototypeBeanProvider.get();
            prototypeBean.addCount();
            return prototypeBean.getCount();
        }
    }
````
- ``get()``을 통해서 항상 새로운 프로토타입 빈이 생성되는 것을 확인할 수 있음


<br />

#### 정리
- 프로토타입 빈을 언제 사용할까? -> 사용할 때마다 의존관계 주입이 완료된 새로운 객체가 필요할 때 (실무에서 사용할 일이 드물긴 함)
- ObjectProvider, JSR303 Provider -> 프로토타입 뿐만 아니라 DL이 필요한 경우는 언제든 사용 가능

<br /><br />

---
### 웹 스코프
#### 종류
- request : HTTP 요청 하나가 들어오고 나갈 때까지 유지되는 스코프, 각 HTTP 요청마다 별도의 빈 인스턴스 생성
- session : HTTP Session과 동일한 생명주기를 가지는 스코프
- application : 서블릭 컨텍스트(ServletContext)와 동일한 생명주기를 가지는 스코프
- websocket

````java
@Controller
@RequiredArgsConstructor
public class LogDemoController {

    private final LogDemoService logDemoService;
    private final ObjectProvider<MyLogger> myLoggerProvider;

    @RequestMapping("log-demo")
    @ResponseBody
    public String logDemo(HttpServletRequest request) {
        String requestURL = request.getRequestURL().toString();

        MyLogger myLogger = myLoggerProvider.getObject();
        myLogger.setRequestURL(requestURL);

        myLogger.log("controller test");
        logDemoService.logic("testId");

        return "OK";
    }
}
````
````shell
[0401f29e-...] request scope bean create: hello.core.common.MyLogger@2d84e23
[0401f29e-...][http://localhost:8080/log-demo] controller test
[0401f29e-...][http://localhost:8080/log-demo] service id = testId
[0401f29e-...] request scope bean close: hello.core.common.MyLogger@2d84e23
````

- ObjectProvider를 사용해서 ``getObject()`` 호출 시점까지 request scope 빈의 생성을 지연할 수 있음
  - 그냥 MyLogger 사용하면 빈의 생성 도중에 호출해서 오류남
- LogDemoController, LogDemoService 내에 ``getObject()`` 각각 호출해도 같은 HTTP 요청이면 같은 스프링 빈이 반환됨

---
### 스코프와 프록시
````java
@Component
@Scope(value = "request", proxyMode = ScopedProxyMode.TARGET_CLASS)
public class MyLogger {
  ...
}
````
````shell
myLogger =class hello.core.common.MyLogger$$SpringCGLIB$$0
````
- **CGLIB라는 라이브러리로 내 클래스를 상속 받은 가짜 프록시 객체를 만들어서 주입한다.**
- 가짜 프록시 객체는 요청이 오면 내부에서 진짜 빈을 요청하는 위임 로직이 들어있음