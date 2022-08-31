### 0831

# CSS-3 

### 1.position 속성

`position` 속성은 태그를 어떻게 위치시킬지를 정의

- `static` : 모든 태그의 기본 값(기준 위치)

  - 일반적인 요소의 배치 순서에 따름(좌측 상단) 
  - 부모 요소 내에서 배치될 때는 부모 요소의 위치를 기준으로 배치 됨

- `relative` : 상대 위치

  - 자기 자신의 static 위치를 기준으로 이동 (normal flow 유지)
  - 레이아웃에서 요소가 차지하는 공간은 static일 때와 같음 (normal position 대비 offset)

- `absolute` : 절대 위치

  - 요소를 일반적인 문서 흐름에서 제거 후 레이아웃에 공간을 차지하지 않음 (normal flow에서 벗어남) 
  - static이 아닌 가장 가까이 있는 부모/조상 요소를 기준으로 이동 (없는 경우 브라우저 화면 기준으로 이동)

- `fixed` : 고정 위치

  - 요소를 일반적인 문서 흐름에서 제거 후 레이아웃에 공간을 차지하지 않음 (normal flow에서 벗어남) 
  - 부모 요소와 관계없이 viewport를 기준으로 이동 / 스크롤 시에도 항상 같은 곳에 위치함

- `sticky`: 스크롤에 따라 `static` -> `fixed`로 변경

  -  속성을 적용한 박스는 평소에 문서 안에서 position: static 상태와 같이 일반적인 흐름에 따르지만 

    스크롤 위치가 임계점에 이르면 position: fixed와 같이 박스를 화면에 고정할 수 있는 속성

  - 일반적으로 Navigation Bar에서 사용됨

좌표를 지정 해주기 위해서는 `left`, `right`, `top`, `bottom` 속성과 함께 사용

`position`을 `absolute`나 `fixed`로 설정시 가로 크기가 100%가 되는 `block` 태그의 특징이 사라짐

```css
#box1 { position:static }
#box2 { position:absolute }
#box3 { position:relative }
#box4 { position:fixed }
```

```html
<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
  <link rel="stylesheet" href="0831.css">
</head>
<body>
	<div class="box-container">
		<div id="box1">static 박스</div>
		<div id="box2">relative 박스</div>
		<div id="box3">absolute 박스</div>
		<div id="box4">fixed 박스</div> <!-- '출력 결과' 란이 아닌, 전체 페이지에서 고정되어 보여짐 -->
	</div>
</body>
</html>
```

```css
.box-container{
  width: 350px;
  border: 2px solid #e91bf5;
}
.box-container div{
  padding: 10px;
  border: 1px solid green;
  background-color: #e3ffe0;
}
#box1 { position: static; top: 20px; left: 30px; }
#box2 { position: relative; top: 20px; left: 30px; }
#box3 { position: absolute; top: 20px; right: 30px; }
#box4 { position: fixed; top: 20px; right: 30px; }
```

![position](/Users/yoonji_kim/Desktop/WEB/WEB03/0831/position.png)

#### 1-1.absolute와 relative

`relative` 인 컨테이너 **내부**에 `absolute`인 객체가 있으면 절대 좌표를 계산할 때, `relative` 컨테이너를 기준점으로 잡게 됩니다. (없다면 전체 문서가 기준)

- `absolute`는 normal flow에서 벗어남. 즉 다음 블록 요소가 좌측 상단으로 붙음.
- `relative`는 normal flow 유지. 실제 위치는 그대로, 사람 눈에만 이동

```html
<html>
<head>
	<style>
		#box-container{ position: relative; height: 90px; margin-top: 40px; border: 2px solid red; }
		#box-inner{ position: absolute; top: 30px; left: 20px; border: 2px solid blue; }
	</style>
</head>
<body>
	<div id="box-container">
		컨테이너
		<div id="box-inner">absolute 박스</div>
	</div>
</body>
</html>
```

![컨테이너](/Users/yoonji_kim/Desktop/WEB/WEB03/0831/컨테이너.png)



### ⭐️CSS 원칙⭐️ 잊지말자!!

- **CSS 원칙 I, II : Normal flow** 
  - • 모든 요소는 네모(박스모델), 좌측상단에 배치
  -  display에 따라 크기와 배치가 달라짐 
- **CSS 원칙 III** 
  - position으로 위치의 기준을 변경 
    - relative : 본인의 원래 위치 
    - absolute : 특정 부모의 위치 
    - fixed : 화면의 위치 
    - sticky: 기본적으로 static이나 스크롤 이동에 따라 fixed로 변경

------------------------------

### 2.float 속성

`float` 라는 단어는 원래 ‘뜨다’ 라는 의미이며, 원래 웹페이지에서 **이미지**를 어떻게 띄워서 텍스트와 함께 배치할 것인가에 대한 속성입니다.

<img src="/Users/yoonji_kim/Desktop/WEB/WEB03/0831/float.gif" alt="float" style="zoom:100%;" />

- `inherit`: 부모 요소에서 상속
- `left`: 왼쪽에 부유하는 블록 박스를 생성. 페이지 내용은 박스 오른쪽에 위치하며 위에서 아래로 흐름.
- `right`: 오른쪽에 부유하는 블록 박스를 생성. 페이지 내용은 박스 왼쪽에 위치하며 위에서 아래로 흐름. 이후 요소에 clear 속성이 있으면 페이지 흐름이 달라짐. none 이 아니라면 display 속성은 무시된다.
- `none` - 요소를 부유시키지 않음
- 박스를 왼쪽 혹은 오른쪽으로 이동시켜 텍스트를 포함 인라인요소들이 주변을 wrapping 하도록 함 
- 요소가 Normal flow를 벗어나도록 함

`left`와 `right`를 통해 부유속성을 지정시 `display`는 무시됩니다. (`none`은 제외)
또한 이후 요소에 [`clear`](https://ofcourse.kr/css-course/clear-속성) 속성이 있으면 페이지 흐름이 달라집니다.

```css
.box {
  width: 150px;
  height: 150px;
  border: 1px solid black;
  background-color: crimson;
  color: white;
  margin-right: 30px;
  }
  .left {
  float: left;
  }
  .p {
    font:bold;
    font-size: 30px;
  }
```

```html
<boby>
  <br><div class="box left">float left</div>
    <p class="p">Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod
      tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam,
      quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo
      consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse
      cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non
      proident, sunt in culpa qui officia deserunt mollit anim id est laborum.</p>
</boby> 
```

![float-left](/Users/yoonji_kim/Desktop/WEB/WEB03/0831/float-left.png)

-----------------------------------

### 3.Flex 속성

- 배치 설정 
  - `flex-direction`
  - `flex-wrap` 
-  공간 나누기 
  - `justify-content` (main axis) 
  - `align-content` (cross axis) 
- 정렬 
  - `align-items` (모든 아이템을 cross axis 기준으로) 
  - `align-self `(개별 아이템)



#### 3-1. flex-direction

- Main axis 기준 방향 설정 
- 역방향의 경우 HTML 태그 선언 순서와 시각적으로 다르니 유의 (웹 접근성에 영향)![flex-direction](/Users/yoonji_kim/Desktop/WEB/WEB03/0831/flex-direction.png)

#### 3-2. flex-wrap

- 아이템이 컨테이너를 벗어나는 경우 해당 영역 내에 배치되도록 설정 
- 즉, 기본적으로 컨테이너 영역을 벗어나지 않도록 함
- `nowrap` (기본 값) : 한 줄에 배치 
- `wrap` : 넘치면 그 다음 줄로 배치

<img src="/Users/yoonji_kim/Desktop/WEB/WEB03/0831/flex-wrap.png" alt="flex-wrap" style="zoom:45%;" />

#### 3-3. flex-flow

- flex-direction 과 flex-wrap 의 shorthand 
- flex-direction과 flex-wrap에 대한 설정 값을 차례로 작성 
  - 예시) flex-flow: row nowrap;



#### 3-4. justify-content

- Main axis를 기준으로 공간 배분

![justify-content](/Users/yoonji_kim/Desktop/WEB/WEB03/0831/justify-content.png)



#### 3-5.  justify-content & align-content

- 공간 배분 
  - `flex-start` (기본 값) : 아이템들을 axis 시작점으로 
  - `flex-end` : 아이템들을 axis 끝 쪽으로 
  - `center` : 아이템들을 axis 중앙으로 
  - `space-between` : 아이템 사이의 간격을 균일하게 분배 
  - `space-around` : 아이템을 둘러싼 영역을 균일하게 분배 (가질 수 있는 영역을 반으로 나눠서 양쪽에) 
  - `space-evenly` : 전체 영역에서 아이템 간 간격을 균일하게 분배



#### 3-6.  align-items

- 모든 아이템을 Cross axis를 기준으로 정렬

![align-items](/Users/yoonji_kim/Desktop/WEB/WEB03/0831/align-items.png)



#### 3-7. align-self

- 개별 아이템을 Cross axis 기준으로 정렬 
  - 주의! 해당 속성은 컨테이너에 적용하는 것이 아니라 개별 아이템에 적용

![align-self](/Users/yoonji_kim/Desktop/WEB/WEB03/0831/align-self.png)

#### 3-8. align-items & align-self

- Cross axis를 중심으로 • 
  - `stretch` (기본 값) : 컨테이너를 가득 채움 
  - `flex-start` : 위 
  - `flex-end` : 아래 
  - `center` : 가운데 
  - `baseline` : 텍스트 baseline에 기준선을 맞춤



#### 3-9. 기타

- `flex-grow` : 남은 영역을 아이템에 분배 
- `order` : 배치 순서
  - 0이 기본. 음수와 양수로 설정가능