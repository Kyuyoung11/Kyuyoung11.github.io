---
layout: post
title: "[김영한의 실전 자바] 중급 1편 - 강의를 시작하며"
categories: 
  - Java
  - Intermediate

tags: [자바 중급, 인프런]

toc: true
toc_sticky : true

date: 2024-10-11
last_modified_at: 2024-10-11
---

## 섹션 8. 의존관계 자동 주입


---
### 다양한 의존관계 주입 방법
#### 생성자 주입
- 특징
  - 생성자 호출시점에 딱 한 번만 호출되는 것이 보장
  - 불변(외부에서 수정 불가능)
  - 필수

````java
    @Autowired
    public OrderServiceImpl(MemberRepository memberRepository, DiscountPolicy discountPolicy) {
        this.memberRepository = memberRepository;
        this.discountPolicy = discountPolicy;
    }
````

- 주의 : 생성자가 두개이상이면 ``@Autowired``를 꼭 지정해줘야한다.

<br /><br />

---
#### 수정자 주입
- setter라 불리는 필드의 값을 변경하는 수정자 메서드를 통해서 주입
````java
    private MemberRepository memberRepository;
    private DiscountPolicy discountPolicy;

    @Autowired
    public void setMemberRepository(MemberRepository memberRepository) {
        System.out.println("memberRepository = " + memberRepository);
        this.memberRepository = memberRepository;
    }

    @Autowired
    public void setDiscountPolicy(DiscountPolicy discountPolicy) {
        this.discountPolicy = discountPolicy;
    }
````

<br /><br />

---
#### 필드 주입
- 필드에 바로 ``@Autowired`` 지정

````java
    @Autowired private MemberRepository memberRepository;
    @Autowired private DiscountPolicy discountPolicy;
````
<br />
- 권장하지 않는 방법임
  - 이유 : 외부에서 값을 바꿀 방법이 없음. 
- 사용해도 되는 경우
  - 테스트 코드

<br /><br />

---
#### 일반 메서드 주입
- 아무 메서드에 ``@Autowired`` 지정
- 특징
  - 장점 : 한번에 여러 필드를 주입 받을 수 있다.
  - 일반적으로 잘 사용하지 않는 방법

---
#### 참고
- 생성자 주입은 빈 등록을 하면서 자연스럽게 일어남 (객체를 만들면 생성자를 부를 수 밖에 없으니...) 
- ``@Autowired`` 주입할 대상이 없으면 오류 발생
- 스프링 컨테이너가 관리하는 스프링 빈이어야 주입할 수 있음 (아무 객체나 되지 않음~)


<br/><br/><br/>

---
### 옵션 처리
- 스프링 빈이 없어도 동작해야할 때가 있다.

<br />

**방법 (Member는 스프링빈이 아님)**

````java
public class AutowiredTest {
    @Test
    void AutowiredOption() {
        ApplicationContext ac = new AnnotationConfigApplicationContext(TestBean.class);
    }

    static class TestBean {
        @Autowired(required = false)
        public void setNoBean1(Member noBean1) { 
            System.out.println("noBean1 = " + noBean1);
        }

        @Autowired
        public void setNoBean2(@Nullable Member noBean2) {
            System.out.println("noBean2 = " + noBean2);
        }

        @Autowired
        public void setNoBean3(Optional<Member> noBean3) {
            System.out.println("noBean3 = " + noBean3);
        }
    }
    
}
````


<br/>

**실행결과**
````java
noBean2 = null
noBean3 = Optional.empty
````
- noBean1 - 아예 호출이 안된 것을 확인 할 수 있음
- noBean2 - 호출은 되지만 null로 리턴됨
- noBena3 - Optional로 감싸져서 나옴


<br/><br/><br/>

---
### 생성자 주입을 선택해라!
- 최근에는 생성자 주입을 권장하는 추세 

<br />

**생성자 주입을 선택해야하는 이유**
- 불변
  - 대부분의 의존관계 주입은 한번 일어나면 변경할 일이 없음.
  - 누군가의 실수로 set메서드를 통해 바뀌게 하면 안된다.
- 누락
  - 단위 테스트할 때 수정자 주입인 경우
- final 키워드
  - 필드에 final 키워드를 넣을 수 있다. -> 값이 설정되지 않아 발생하는 오류를 컴파일 시점에 막을 수 있다.

<br /><br />

#### 결론
- 기본적으로는 생성자 주입을 사용, 필수 값이 아닌 경우에는 수정자 주입 방식을 옵션을 부여 (동시 사용 가능)
- 필드 주입은 사용하지 않는게 좋다!

<br /><br /><br /><br />

----
### 롬복과 최신 트렌드

````java
@Component
public class OrderServiceImpl implements OrderService {
    private final MemberRepository memberRepository;
    private final DiscountPolicy discountPolicy;

    /**
     * 생성자 주입 -> lombok @RequiredArgsConstructor 으로 대체 가능 (final 멤버변수)
     */
    @Autowired
    public OrderServiceImpl(MemberRepository memberRepository, DiscountPolicy discountPolicy) {
        this.memberRepository = memberRepository;
        this.discountPolicy = discountPolicy;
    }
  ...
}
````
- 여기서 생성자를 ``@RequiredArgsConstructor`` 애노테이션으로 대체 가능함
  - final이 붙은 필드를 모아서 생성자를 자동으로 만들어줌

<br/>

![]({{site.baseurl}}/images/4/240906_1.png)
- Ctrl + F + F12를 눌러서 생성자가 클래스 정보에 뜨는걸 확인 할 수 있음


<br /><br /><br /><br />

----
### 조회 빈이 2개 이상 - 문제
- 오류 발생, DIP를 위배함, 유연성 떨어짐
- ``NoUniqueBeanDefinitionException`` 오류 발생

<br /><br /><br /><br />

---
### @Autowired 필드명 매칭
1. 타입 매칭
2. 타입 매칭 결과가 2개 이상이면, 파라미터 명으로 빈 이름 매칭


<br /><br />

### @Qualifier 사용

````java
@Component
@Qualifier("mainDiscountPolicy")
public class RateDiscountPolicy implements DiscountPolicy {
  ...
}


@Component
//@RequiredArgsConstructor
public class OrderServiceImpl implements OrderService {
    private final MemberRepository memberRepository;
    private final DiscountPolicy discountPolicy;


    @Autowired
    public OrderServiceImpl(MemberRepository memberRepository, @Qualifier("mainDiscountPolicy") DiscountPolicy discountPolicy) {
        this.memberRepository = memberRepository;
        this.discountPolicy = discountPolicy;
    }
    
  ...
}
````

1. @Qualifier 매칭
2. 스프링빈이름으로 매칭

- 단점 : 모든 코드에 ``@Qualifier``를 붙여줘야함
- (참고) ``@Qualifier`` 는 스프링빈 매칭말고 ``@Qualifier`` 매칭을 하도록 하는 것이 좋다.

<br /><br />

### @Primary 사용

- 우선순위를 정하는 방법. @Autowired로 여러 개의 빈이 매칭되면, ``@Primary``가 우선순위를 가짐


<br /><br /><br /><br />

---
### Annotation 직접 만들기
1. 클래스 찾기로 @Qualifer 검색
2. 위에 애노테이션 부분 복붙 - @interface 클래스 만들기
3. ``@Qualifier("mainDiscountPolicy)`` 추가
4. 실제로 사용할 땐 ``@MainDiscountPolicy`` 로 불러오면 됨

````java
@Target({ElementType.FIELD, ElementType.METHOD, ElementType.PARAMETER, ElementType.TYPE, ElementType.ANNOTATION_TYPE})
@Retention(RetentionPolicy.RUNTIME)
@Inherited
@Documented
@Qualifier("mainDiscountPolicy")
public @interface MainDiscountPolicy {
}
````

````java
@Component
@MainDiscountPolicy
public class RateDiscountPolicy implements DiscountPolicy{
  ...
}
````

<br /><br /><br /><br />

---
### 조회한 빈이 모두 필요할 때 - List, Map
- 동적으로 빈을 선택해야할 때, 모든 빈을 받아서 그때 그때 적절한걸 반환하도록 할 수 있다.

<br /><br /><br /><br />

---
### 자동, 수동의 올바른 실무 운영 기준
- 기본적으로는 자동을 쓰기
- 직접 등록하는 기술 지원 객체는 수동 등록 -> 코드만 보고 파악하기 쉬움
- 다형성을 적극 활용하는 비즈니스 로직은 수동 등록을 고민해보기 -> 자동으로 하면 같은 패키지 내에 두는 것이 좋음

