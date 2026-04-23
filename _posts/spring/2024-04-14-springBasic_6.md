---
layout: post
title: "[Spring] 스프링 핵심 원리 - 기본편 (6) 컴포넌트 스캔"
categories: 
  - Java
  - Spring

tags: [Spring, 인프런]

toc: true
toc_sticky : true

date: 2024-04-14
last_modified_at: 2024-04-14
---

## 섹션 6.컴포넌트 스캔


---
### 컴포넌트 스캔

``@ComponentScan``
- @Component  애노테이션이 붙은 클래스를 스캔해서 스프링 빈으로 등록한다.
- 빈 이름 : 클래스 이름 앞글자를 소문자로 사용 
  - MemberServiceImpl -> memberServiceImpl
- 참고 : 스프링부트를 사용하면 ``@SpringBootApplication`` 안에 이미 @ComponentScan이 들어있음

<br />

```java
@ComponentScan(
        // 탐색할 패키지 지정
        basePackages = "hello.core.member",
        // 제외 필터
        excludeFilters = @ComponentScan.Filter(type = FilterType.ANNOTATION, classes = Configuration.class)
)
```
- basePackages : 탐색할 패키지 지정
  - 지정하지않으면 Config 파일의 패키지 경로
  - 권장하는 방법 : 설정하지 않고, 설정 정보를 프로젝트 최상단에 둠
- excludeFilters : @Configuration이 붙은 클래스는 제외할 수 있음


<br />

<b>컴포넌트 스캔 기본 대상 </b>
- @Component
- @Controller : 스프링 MVC 컨트롤러로 인식
- @Service : 비즈니스 로직이겠거늘 
- @Repository : 스프링 데이터 접근 계층으로 인식, 데이터 계층의 예외를 스프링 예외로 변환해준다.
- @Configuration : 스프링 설정 정보, 스프링 빈이 싱글톤을 유지하도록 추가 처리

<br />
<br />
<br />

----
### AutoWired 의존관계 자동 주입 

``@Autowired``
- 생성자에 애노테이션을 지정하면, 스프링 컨테이너가 자동으로 해당 스프링 빈을 찾아서 주입함



<br />
<br />
<br />

