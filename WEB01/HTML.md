### 0829

# HTML (Hyper Text Markup Language)

### HTML기초

👉 [Mozilla](https://developer.mozilla.org/ko/docs/Web/HTML) , [w3schools](https://www.w3schools.com/html/default.asp)

> Markup Language - 태그 등을 이용하여 문서나 데이터의 구조를 명시하는 언어 ex)– HTML, Markdown
>
> HTML - 웹 페이지를 작성(구조화)하기 위한 언어/ 뒤에 .html을 붙여주면 파일생성

```html
<!DOCTYPE html> --> 이 문서가 html이라는걸 알려줌
<html> --> HTML 페이지의 루트 요소
<head> --> HTML 페이지에 대한 메타 정보가 포함 
  (문서 제목, 인코딩, 스타일, 외부 파일 로딩 등,일반적으로 브라우저에 나타나지 않는 내용)
<title>Page Title</title> --> HTML 페이지의 제목을 지정합니다(브라우저의 제목 표시줄 또는 페이지의 탭에 표시됨)
</head> 
<body>-->본문을 정의하며 표제, 단락, 이미지, 하이퍼링크, 표, 목록 등과 같이 보이는 모든 내용을 담는 컨테이너

<h1>KYJ</h1> --> 큰 제목을 정의
<p>My first HTML.</p> --> 단락을 정의

</body>
</html>
```



- **head 예시**

  ```html
  - <title> : 브라우저 상단 타이틀
  - <meta> : 문서 레벨 메타데이터 요소  
  - <link> : 외부 리소스 연결 요소 (CSS 파일, favicon 등)
  - <script> : 스크립트 요소 (JavaScript 파일/코드)
  - <style> : CSS 직접 작성
  
  -----------------------------------
    
  <head>
  	<title>HTML 수업</title>
  	<meta charset="UTF-8">
  	<link href="style.css" rel="stylesheet">
  	<script src="javascript.js"></script>
  	<style>
  		p {
  			color: black;
  		}
  	</style>
  </head>
  ```

  

- **요소 (element)**
  - HTML 요소는 시작 태그와 종료 태그 그리고 태그 사이에 위치한 내용으로 구성
  - 요소는 태그로 컨텐츠(내용)를 감싸는 것으로 그 정보의 성격과 의미를 정의
  - 내용이 없는 태그들도 존재(닫는 태그가 없음) `br`,` hr`, `img`, `input`, `link`, `meta`
  - 요소는 중첩(nested)될 수 있음/ 요소의 중첩을 통해 하나의 문서를 구조화
  - 여는 태그와 닫는 태그의 쌍을 잘 확인해야함
  - 오류를 반환하는 것이 아닌 그냥 레이아웃이 깨진 상태로 출력되기 때문에, 디버깅이 힘들어 질 수 있음



- **속성(attribute)**
  - 속성을 통해 태그의 부가적인 정보를 설정할 수 있음
  - 요소는 속성을 가질 수 있으며, 경로나 크기와 같은 추가적인 정보를 제공
  - 요소의 시작 태그에 작성하며 보통 이름과 값이 하나의 쌍으로 존재
  - 태그와 상관없이 사용 가능한 속성(HTML Global Attribute)들도 있음
  - `<a href = ''https://google.com"></a>`      여기서 `href`는 속성명,  `구글주소`는 속성값
  - 태그별로 사용할 수 있는 속성은 다르다.
  - 공백은 X ,` '' '' `쌍따옴표 사용하기.
  - *HTML Global Attribute*
    - 모든 HTML 요소가 공통으로 사용할 수 있는 대표적인 속성 (몇몇 요소에는 아무 효과가 없을 수 있음)
      - `id` : 문서 전체에서 유일한 고유 식별자 지정
      - `class` : 공백으로 구분된 해당 요소의 클래스의 목록 (CSS, JS에서 요소를 선택하거나 접근)
      - `data-*` : 페이지에 개인 사용자 정의 데이터를 저장하기 위해 사용
      - `style` : inline 스타일
      - `title` : 요소에 대한 추가 정보 지정
      - `tabindex` : 요소의 탭 순서

```html
<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<title>Document</title>
</head>
<body>
	<!-- 이것은 주석입니다. -->
	<h1>나의 첫번째 HTML</h1>
	<p>이것은 본문입니다.</p>
	<span>이것은 인라인요소</span>
<a href="https://www.naver.com">네이버로 이동!!</a>
</body>
```



- **DOM(Document Object Model) 트리**
  - 렌더링(Rendering) - 웹사이트 코드를 사용자가 보게되는 웹 사이트로 바꾸는 과정
  - 텍스트 파일인 HTML 문서를 브라우저에서 렌더링 하기 위한 구조
    - HTML 문서에 대한 모델을 구성함
    - HTML 문서 내의 각 요소에 접근 / 수정에 필요한 프로퍼티와 메서드를 제공함



- **블록요소 (block element)**
  - 사용 가능한 **최대 가로 너비**를 사용함 ( 기본 너비값은 `100%` )
  - 전체를 차지하기 때문에 각 요소들이 **수직으로 쌓임** ( 한 줄에 한개만 배치 )
  - **크기값** 가질 수 있음 ( 가로 너비 & 세로 길이 지정 가능 )
  - **상하좌우** 마진 & 패딩을 가질 수 있음
  - 레이아웃을 작업하는 요소로 적합
  - < 주요 블록 요소들 >
    `div`　`p`　`ul`　`ol`　`li`　`h1~h6` `form` `header` `nav` `footer` `section` `article` `aside` `table` `th` `td` `figure` `figcaption` `caption` `blockquote`



- **인라인요소 (inline element)**
  - 사용 가능한 **필요한 만큼의 영역**을 사용함 ( 컨텐츠 너비 만큼 )
  - 요소들이 **수평으로 쌓임** ( 한 줄에 여러개 배치 )
  - **크기값** 가질 수 없음 ( 사이즈 지정 불가능 )
  - **상하 마진** 적용 불가능
    ( 좌우 마진은 가능 / 상하좌우 패딩도 가능 )
  - 텍스트를 작업하는 요소로 적합
  - 주요 인라인 요소들
    `span`　`a`　`em` `b` `strong` `video` `audio` 등



- **인라인-블록요소 (inline-block element)**

  - 기본 특성은 인라인이라 요소가 **수평**으로 쌓이지만
    블록 요소처럼 **사이즈를 적용**할 수 있다.
  - **크기값** 가질 수 있음 ( 가로 너비 & 세로 길이 지정 가능 )
  - **상하좌우** 마진 & 패딩을 가질 수 있음
  - 사용 가능한 **필요한 만큼의 영역**을 사용함 ( 컨텐츠 너비 만큼 )
  - 요소들이 **수평으로 쌓임** ( 한 줄에 여러개 배치 ) 
  - ` ( width / height / margin-top / margin-bottom 적용 가능 )`
  - 주요 인라인 블록 요소들
    `img` `input` `button`

  

- **텍스트요소**
  - `<a></a>` :  href 속성을 활용하여 다른 URL로 연결하는 하이퍼링크 생성
  - `<b></b>`  : 굵은 글씨 요소
  - `<strong></strong>` : 중요한 강조하고자 하는 요소 (보통 긁은 글씨로 표현)
  - `<i></i>` : 기울임 글씨 요소
  - `<em></em>` : 중요한 강조하고자 하는 요소 (보통 기울임 글씨로 표현)
  - `<br>` : 텍스트 내에 줄 바꿈 생성
  - `<img>` : src 속성을 활용하여 이미지 표현, alt 속성을 활용하여 대체 텍스트
  - `<span></span>` : 의미 없는 인라인 컨테이너



- **그룹 컨텐츠**
  - `<p></p>` : 하나의 문단 (paragraph)
  - `<hr>` : 문단 레벨 요소에서의 주제의 분리를 의미하며 수평선으로 표현됨 (A Horizontal Rule)
  - `<ol></ol>` : 순서가 있는 리스트 (ordered)
  - `<ul></ul>` : 순서가 없는 리스트 (unordered)
  - `<pre></pre>` : HTML에 작성한 내용을 그대로 표현. 보통 고정폭 글꼴이 사용되고 공백문자를 유지
  - `<blockquote></blockquote>` : 텍스트가 긴 인용문. 주로 들여쓰기를 한 것으로 표현됨
  - `<div></div>` : 의미 없는 블록 레벨 컨테이너



