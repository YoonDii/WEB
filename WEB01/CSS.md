### 0829

# CSS (Cascading Style Sheets)

> 스타일을 지정하기 위한 언어

<img src="/Users/yoonji_kim/Library/Application Support/typora-user-images/스크린샷 2022-08-29 오후 4.44.47.png" alt="스크린샷 2022-08-29 오후 4.44.47" style="zoom:30%;" />

> - CSS 구문은 선택자를 통해 스타일을 지정할 HTML 요소를 선택
>
> - 중괄호 안에서는 속성과 값, 하나의 쌍으로 이루어진 선언을 진행
>
> - 각 쌍은 선택한 요소의 속성, 속성에 부여할 값을 의미
>   - 속성 (Property) : 어떤 스타일 기능을 변경할지 결정
>   - 값 (Value) : 어떻게 스타일 기능을 변경할지 결정.



> - CSS 정의방법
>   - 인라인(inline)
>   - 내부 참조(embedding) - `<style>`
>   - 외부 참조(link file) – 분리된 CSS 파일

```css
/*인라인*/
<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	<title>Document</title>
</head>
<body>
	<h1 style="color: blue; font-size: 100px;">Hello</h1>
</body>
</html>

/*내부참조*/
<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	<title>Document</title>
	<style>
		h1 {
			color: blue;
			font-size: 100px;
		}
	</style>
</head>
<body>
</body>
</html>

/*외부참조
외부 CSS파일 <head>내 <link>를 통해 불러오기*/

```



> - 기초 선택자
>   - 요소 선택자
>     - HTML 태그를 직접 선택
>   - 클래스(class) 선택자
>     - 마침표(.)문자로 시작하며, 해당 클래스가 적용된 항목을 선택
>   - 아이디(id) 선택자
>     - \# 문자로 시작하며, 해당 아이디가 적용된 항목을 선택
>     - 일반적으로 하나의 문서에 1번만 사용
>     - 여러 번 사용해도 동작하지만, 단일 id를 사용하는 것을 권장
>   - 우선순위 차례로 적용
>     - id > class > tag 순 / 우선순위 높은게 먼저 적용
>     - id는 주로 자바스크립트에서 사용
>     - Id는 하나만 사용하는 것이 나중에 안헷갈림.



