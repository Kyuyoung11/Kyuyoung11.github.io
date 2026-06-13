---
layout: post
title: "[Claude Code] Claude Code로 서점 웹 만들기 - 테스트 코드 & 장바구니 기능"
categories:
  - AI
  - ClaudeCode

tags: [ClaudeCode, AI, SpringBoot, Java]

toc: true
toc_sticky : true

date: 2026-06-10
last_modified_at: 2026-06-10
---

> 기존에 Android 앱용으로 만들어두었던 Spring Boot REST API 서버를 클로드 코드를 활용해서 웹 서비스로 확장해보았다.  
> 이 글은 그 과정에서 진행한 작업들을 기록한 경험 공유 글이다.

<br>

---
## 프로젝트 소개

**storeApp-API_Server**는 온라인 서점 기능을 제공하는 Spring Boot REST API 서버다.  
원래는 Android 앱과 통신하기 위해 만든 서버인데, Claude Code를 활용해서 웹 브라우저에서도 직접 사용할 수 있도록 확장해보았다.

**기본 기능**
- 회원가입 / 로그인
- 상품(책) 목록 조회 및 키워드 검색
- 장바구니 조회 / 추가 / 삭제

<br><br>

---
## Claude Code로 한 작업들

### 1. CLAUDE.md 작성

Claude Code를 본격적으로 활용하기 전에 먼저 `CLAUDE.md` 파일을 만들었다.  
이 파일은 Claude Code가 프로젝트를 처음 읽을 때 참고하는 가이드 문서다.

작성한 내용:
- 프로젝트 개요
- 실행 / 테스트 / 빌드 명령어
- DB 연결 정보
- 아키텍처 구조
- API 엔드포인트 목록
- 알려진 이슈 목록

````markdown
## Architecture
레이어드 아키텍처: Controller → Service (interface + impl) → Repository → MySQL

- Entity: AbstractEntity(공통 id/equals/hashCode) → User, Product 상속
- 관계: User ↔ Product ManyToMany, 중간 테이블명 cart (컬럼: userID, bookID)
````

CLAUDE.md를 잘 써두면 매번 프로젝트 구조를 설명하지 않아도 되고, 일관된 방식으로 작업을 진행할 수 있다.

<br>

### 2. 테스트 코드 작성

기존 코드에 테스트가 전혀 없었는데, Claude Code에게 단위 테스트를 작성해달라고 했다.

"UserServiceImpl, ProductServiceImpl, CartController에 대한 단위 테스트를 작성해줘. DB 없이 실행 가능하게 Mockito로 작성해줘."

그러자 아래와 같은 구조로 테스트 파일 3개를 만들어줬다.

````java
@ExtendWith(MockitoExtension.class)
class UserServiceImplTest {

    @Mock
    private UserRepository userRepository;

    @InjectMocks
    private UserServiceImpl userService;

    @Test
    void createUser_저장후_반환() {
        given(userRepository.save(any(User.class))).willReturn(user);

        User result = userService.createUser("testUser", "1234");

        assertThat(result.getName()).isEqualTo("testUser");
    }

    @Test
    void checkNameExists_존재하면_true() {
        given(userRepository.findByName("testUser")).willReturn(Optional.of(user));

        boolean exists = userService.checkNameExists("testUser");

        assertThat(exists).isTrue();
    }
}
````

`@SpringBootTest`는 MySQL 연결이 필요하기 때문에, DB 없이 실행하려면 `@ExtendWith(MockitoExtension.class)` + `@Mock` / `@InjectMocks` 조합을 쓰는 게 맞다.  
이 부분도 Claude Code가 CLAUDE.md에 명시된 내용을 보고 알아서 Mockito 방식으로 작성해줬다.

<br>

### 3. 웹 프론트엔드 추가

기존 REST API 서버에 정적 HTML 파일을 추가해서 브라우저에서 바로 서비스를 사용할 수 있도록 만들었다.

추가된 파일:
- `static/index.html` — 메인 페이지 (책 목록, 검색)
- `static/login.html` — 로그인 페이지
- `static/css/style.css` — 공통 스타일
- `DataInitializer.java` — 앱 실행 시 테스트 데이터 자동 삽입

"로그인 화면과 메인 화면을 HTML/CSS로 만들어줘. API는 기존 REST API를 fetch로 호출하게 해줘."

별도의 프론트엔드 프레임워크 없이, 순수 HTML + fetch API 방식으로 간단하게 구현됐다.  
사용자 정보는 `localStorage`에 저장해서 로그인 상태를 유지하는 방식이다.

<br>

### 4. 장바구니 추가/삭제 기능 구현

기존에 장바구니 **조회** API만 있었고, **추가/삭제** 기능이 없었다.

"장바구니 추가/삭제 API를 만들고, 화면에서도 버튼으로 동작하게 해줘."

Claude Code가 수정/생성한 파일:
- `CartController.java` — 추가/삭제 엔드포인트 추가
- `CartService.java` — 인터페이스에 메서드 추가
- `CartServiceImpl.java` — 실제 로직 구현
- `cart.html` — 장바구니 화면 (추가/삭제 버튼 포함)

````java
// CartController.java - 장바구니 추가
@PostMapping("/{userId}/{productId}")
public ResponseEntity<?> addToCart(@PathVariable Long userId,
                                   @PathVariable Long productId) {
    cartService.addToCart(userId, productId);
    return ResponseEntity.ok().build();
}

// CartController.java - 장바구니 삭제
@DeleteMapping("/{userId}/{productId}")
public ResponseEntity<?> removeFromCart(@PathVariable Long userId,
                                        @PathVariable Long productId) {
    cartService.removeFromCart(userId, productId);
    return ResponseEntity.ok().build();
}
````

<br><br>

---
## Claude Code 사용 소감

**좋았던 점**

테스트 코드 작성이 정말 간편했다.  
간단한 테스트 코드는 솔직히 작성하기 귀찮은 편인데, 테스트 케이스까지 알아서 짜주니 훨씬 수월했다.  
그리고 구현하고 싶은 내용만 명확하게 전달하면 세부 구조는 Claude Code가 알아서 맞춰준다는 점도 좋았다.  
어떻게 구현할지 몰라도, 무엇을 만들고 싶은지만 알면 된다.

<br>

**신경 쓰인 점**

반대로 말하면, 내가 원하는 테스트 케이스를 정확하게 인지하고 있지 않으면 누락하기 쉽다는 생각이 들었다.  
"알아서 해준다"는 게 장점이지만, 그만큼 내가 검토를 소홀히 하면 빠진 케이스를 모르고 넘어갈 수 있다.  
적극적으로 활용하되, 결과물을 꼼꼼히 확인하는 습관이 필요할 것 같다.

<br>

**결론**

기존에 만들어두었던 API 서버를 웹 서비스로 확장하는 작업을 Claude Code를 활용해 하루 안에 마무리할 수 있었다.  
Claude Code는 잘 쓰면 강력한 도구지만, 결국 방향을 잡고 결과를 검증하는 건 사람의 몫이다.

<br><br>
