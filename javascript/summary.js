//## 후행,선행 연산
a = 10;
b = a++; //b=10, a=11 후행연산
b = ++a; //b=12, a=12 //선행연산

//##호이스팅(JS에서만 허용, 게양, 위로 끌어올려짐) ==> 그래서 let을 사용함.
console.log(a) //undefined => var a 가 호이스팅 되어서 a는 인식하지만, 값의 호이스팅까지는 일어나지않음
a = 9; //할당됨
console.log(a); //9 
var a = 10; // 값 재할당
console.log(a); // 10
console.log(a + b); //NaN => 10 + undefined
var b = 20;
console.log(a + b); //30

// 매개변수(parameter) : 함수 선언 시 데이터를 전달받기 위한 변수
// 인자(argument) : 함수 호출시 매개변수에 넘겨주는 값, 함수에서 인자를 매개변수로 받을 때 arguments 예약어로 받은 매개변수를 모두 확인할 수 있음

// var : 호이스팅O, 중복선언O, 함수스코프만 지원, 다른 블록스코프들은(if,for) 스코프를 지원하지않음
// let, const : 호이스팅 X, 중복선언X, 함수,if,for 등 블록스코프 지원
// let, const로 선언한 전역변수는 window객체의 프로퍼티가 아니다. 
// ex) let foo = 1 => window.foo (X) var선언은 window객체의 프로퍼티이다. 

// const는 선언과 동시에 초기화(할당)이 되어야 함(재할당 금지), 일반적으로 상수는 대문자로 선언하고 언더스코어로 구분(스네이크) ex) const TAX_RATE = 0.1
// const로 객체를 선언한 경우는 프로퍼티 키값을 변경할 수 있고 프로퍼티를 추가,삭제할 수 있다. 단 person객체 자체를 삭제할 순 없다.
const person = { name: 'lee' } 
person.name = 'Kim'
console.log(person) // {name:'Kim'}

// 재할당이 필요한 경우 let을 사용하고 최대한 스코프를 좁게 만들어야 한다. 

// Heap, Stack 메모리 : 각각의 저장 공간이 다름, 따라서 변수명이 같아도 위치에 따라 저장공간이 분리됨으로 에러가 나지 않음
// Heap : 어플리케이션이 구동되는 동안 사용되는 메모리, 전역변수 저장
// Stack : 함수 실행시 사용되는 메모리, 함수 종료 시 함수 관련 지역변수들은 제거됨, first in last out
let name = "힙"; //전역변수는 Heap 메모리에 저장
function myFunc() {
    let name = "스택"; //지역변수는 Stack 메모리에 저장
    console.log(name);
}

//## 함수 표현식
//즉시실행함수 : 선언과 동시에 호출
(function() {
    console.log("공부 열심히!")
})();

//일반함수 : function 예약어, func 식별자
function func(매개변수) {
    //함수body
}

//익명함수 : 식별자가 없는 함수, 매개변수로 함수를 전달할 때 사용할 수 있음. 콜백에서 많이 사용
let sum = function (par1, par2) {
    return par1 + par2;
};
sum(10, 20);

//다른 함수의 매개변수에 대입되어 사용되는 경우..
function myFun4(argFun) {
    let result = argFun(10, 20)
    console.log("result:" + result) //30
}
myFun4(function (no1, no2) {
    return no1 + no2;
})

//화살표함수 : 익명함수의 축약형으로 볼 수 있다. 다른 언어에서는 Lambda 함수라고 부름
//(매개변수) => { 함수body } : 매개변수 1개일 경우 () 생략가능, 함수body가 한줄이고 return문이라면 {} 생략가능, para => a + b
let myFunc1 = (no1, no2) => no1 + no2
myFunc1(10, 20)
//hof(high order function)에서 주로 사용 : 다른함수를 매개변수로 받아들이는 함수, 함수를 결과로 리턴하는 함수


// ## 패러다임의 변화
// 절차 지향(알고리즘 위주) ==> 객체 지향(OOP: Object Oriented Programming => JAVA,javascript) ==> Functional Programming(FP => javascript)

// # First Class Citizen 으로서의 함수 (JAVA에서는 아래의 특징이 없다.)
// - 변수,배열 엘리먼트, 다른 객체의 프로퍼티에 할당될 수 있다. (함수를 data처럼 사용이 가능)
// - 함수의 인자로 전달될 수 있다. 
// - 함수의 결과 값으로 반환될 수 있다. 
// - 리터럴로 생성될 수 있다.  
// - 동적으로 생성된 프로퍼티를 가질 수 있다.

//## window.onload : HTML/xml 파서가 문서를 파싱해서 DOM node객체가 생성되면서 DOM Tree를 만든 후에(JS메모리에 저장) 실행해라 
//스크립트가 head안에 있는 경우, DOM node로 접근하는 스크립트는 window.onload안에서 작성해야 한다. 
window.onload = function () { //비표준
    let a = document.querySelector("#a1")
    //실행
};
window.addEventListener('DOMContentLoaded', function(){ //표준

})
 
//브라우저 자식들(기초객체) : window, document, navigator, history, location
//window 객체의 프로퍼티들 : innerWidth,innerHeight,localStorage,sessionStorage,scrollX,scrollY,parent(팝업을 호출한 부모브라우저, 또는 iframe의 상위html)
//window 객체의 메서드 : alert,confirm,prompt,stop(load 멈추기),open,onload 
//history 객체의 메서드 : back, forward, go(-2) 전전페이지로 이동
//location 객체의 프로퍼티 : href, host, hostname, hash, pathname, port, protocol, search(쿼리값)

//## 객체 : 관련된 변수(프로퍼티),함수(메소드)를 묶은 것, 프로그램에서 인식할 수 있는 모든 대상
// instance (사전적의미:사례) : 객체는 new 키워드를 통해 Date객체의 인스턴스를 만들어 변수에 저장하여 사용한다.
// new는 객체생성 예약어, 뒤에 생성자함수(or 클래스)는 보통 대문자로 시작 
let now = new Date() // Date 내장객체의 인스턴스를 만들어서 now 변수에 저장 
now.toLocaleString() // .은 객체의 멤버접근연산자. Date객체의 toLocaleString메서드를 사용
let dateSet = new Date(2023, 10, 3, 17, 3, 24, 0) //시간을 셋팅해서 생성할때 월은 11로 떨어진다. 0~11의 숫자로 월을 표시하므로 11은 12월임. 월 사용시 -1이 필요.

//property : 객체의 속성
//method : 객체의 동작, 함수이기 때문에 ()붙여야 함. ex)now.toLocaleString()

let array = new Array() //Array 클래스로 array 객체를 생성
let array1 = ['사과','포도','딸기']
array1.forEach((elements) => { //forEach는 매개변수로 함수전달. 배열의 elements갯수만큼 함수를 호출
    console.log(elements)
})
console.log(typeof array1) //object
console.log(array1 instanceof Array) //왼쪽의 객체가 오른쪽의 객체(클래스)로 만든것이냐, true/false 반환

//##Array 객체의 메서드
//every : 배열요소가 주어진 조건에 대해 참이면 true, 거짓이면 false 
let array2 = [1,2,3,4,5]
let result2 = array2.every(element => element > 0) //true
//filter : 조건에 대해 참인 것만 골라 새로운 배열을 만듦 array2.filter((element) => 조건)
//for of : 객체의 for in 의 개념과 같은데, array처럼 length가 있는 객체만 사용 가능하다.
//forEach : 배열요소 갯수만큼 콜백함수를 실행. 리턴 값 없음 forEach(function(값,순서)) 의 순서로 매개변수를 갖는다.
//map : 배열요소 갯수만큼 콜백함수를 실행 후 새로운 배열을 반환함. 리턴 값이 있다. 
let result3 = array2.map((element) => element * 2)
console.log(result3) //[2,4,6,8,10]
//indexOf : 조건에 일치하는 첫 index를 반환
//push : 끝에 추가, unshift : 앞에 추가
//pop : 끝을 반환, shift : [0]을 반환
//splice(index, 삭제할갯수, 추가할데이타) : splice(2) 2부터~마지막까지 삭제, splice(2,1) 2부터 1개만 삭제, splice(2,1,"js") 2부터 1개를 삭제하고 그자리에 "js"를 추가(즉 수정)
//slice : 추출만 하고, 원본배열은 변하지 않음, slice(2) 2부터 마지막까지 추출, slice() 전체 복사 추출
let result4 = array2.slice(2,4) //index 2부터 index3까지 추출
console.log(result4) //3,4
//sort : 정렬 
//toString : 문자열로 반환, ,로 구분해줌
let result5 = array2.toString()
console.log(result5) //'1,2,3,4,5' 문자열 반환

// string은 유사배열로써, index와 length를 가진다. 재할당(주소변경)은 가능하나, 변수[0] = "변경값"을 지정할 순 없다.
// arguments도 유사배열 


//##Math 객체의 메서드 : Math는 인스턴스 생성없이 사용할 수 있다.
//cell() 소수점 이하를 올림
//floor() 소수점 이하를 버림
//round() 소수점 이하를 반올림
//random() 0~1 소수값 추출, 0~100 사이의 랜덤 => Math.floor(Math.random() * 100) / 1~9사이랜덤 Math.random() * (10-1) + 1
//max(), min() 큰수, 작은수

// ##DOM 
//document.querySelectorAll("ul li") ==> NodeList 라는 DOM 컬렉션을 반환
//pageX(스크롤 포함), clientX(스크롤 미포함), screenX(브라우저탭부분까지 포함)
//addEventListener(이벤트, 함수, 캡처 여부) : 캡처여부는 기본이 false(버블링), true(캡처링) / onclick 이벤트함수는 캡처여부를 핸들링할수X
//<div id="부모" onclick="함수"><div id="자식" onclick="함수"></div></div>
//버블링 : node가 중첩되고 이벤트가 각각 있을 경우, 자식에게 클릭이벤트가 발생될 때 부모에게도 클릭이벤트가 발생된다.  event.stopPropagation() //propagation:번식, 버블링을 막음
//캡처링 : 이벤트가 부모에서 자식으로 내려옴
//event.target(실제 이벤트가 발생한 타겟), event.currentTarget(이벤트를 등록한 타겟, a.addEventListener라면 a를 지칭)
//true(캡처링) div1 - div2 - div3 의 순서대로 이벤트 처리
//false(버블링)=> 이게 기본값, 말단자식을 클릭시에 div3 - div2 - div1 의 순서대로 이벤트 처리
let div1 = document.getElementById('div1')
let div2 = document.getElementById('div2')
let div3 = document.getElementById('div3')

div1.addEventListener('click', function(){
    console.log('div1 click')
}, false)

div2.addEventListener('click', function(){
    console.log('div2 click')
}, false)

div3.addEventListener('click', function(event){
    console.log('div3 click')
    // event.stopPropagation() //propagation:번식, 버블링을 막음 'div3 click'만 출력
}, false)


//노드 생성
//0. let div = document.getElementTagName("div") 부모 노드 지정
//1. let p = document.createElement("p") p 노드 생성 
//2. let pAtt = document.createAttribute('style') 속성노드 생성. 
//3. pAtt.value = 'color:red' 속성 값 정의
//4. p.setAttributeNode(pAtt) 속성 셋팅
//5. let pText = document.createTextNode("텍스트추가") 텍스트 노드 생성 
//6. p.appendChild(pText) 텍스트노드 어펜드
//7. div.appendChild(p) 부모노드에 생성한 p노드 어펜드
let div = document.getElementById("nodetest")
let addP = document.createElement("p")
let pAtt = document.createAttribute('style')
let pAtt2 = document.createAttribute('id')
pAtt.value = 'color:red'
pAtt2.value = 'pId'
addP.setAttributeNode(pAtt)
addP.setAttributeNode(pAtt2)
let pText = document.createTextNode("텍스트추가")
addP.appendChild(pText)
div.appendChild(addP)


//노드 삭제
//1. 삭제할 노드의 부모노드 선택 => let node = 삭제할노드.parentNode
//2. 부모노드.removeChild(삭제할노드) => node.removeChild(삭제할노드)
// firstElementChild 는 첫번째 태그(요소) 자식, firstChild는 첫번째의 것(text or "")
// nodeValue : 노드의 값 
document.getElementById('deleteNode').addEventListener('click', function(){
    let myParent = document.getElementById("pId").parentNode
    myParent.removeChild(addP)
})

// 함수명, 함수명() 차이
// 함수() : 실행
// addEventListener('click', 함수명) : addEventListener 함수의 매개변수로써 'click', 함수명이 전달됨. 함수명을 등록해둔 것, 함수명()을 했다면 먼저 실행이 되어버린다.
// function b(par){} 있다면, b(10+20) => 10+20이 먼저 실행되고 b를 호출함. 

//프레임워크 : 원하는 기능 구현에 집중하여 개발할 수 있도록 필요한 기능을 갖추고 있는 것, 일정한 형태를 가지고 다양한 형태의 결과물을 만드는 것
//프로그램이 내 코드를 호출 
//라이브러리 : 공통으로 사용될 수 있는 특정한 기능들을 모듈화한 것, 내 코드가 라이브러리를 호출
//CDN : Content Delivery Network 

//HTML Collection, NodeList 차이
// getElementsByClassName, getElementsByTagName은 HTMLCollection 이라는 DOM 컬렉션을 반환.
// querySelectorAll은 NodeList 라는 DOM 컬렉션을 반환.
// HTMLCollection은 노드의 상태 변화를 실시간으로 감지하고, NodeList는 노드를 정적으로 관리
// 다만 childNodes 가 리턴한 NodeList는 정적임이 보장되지 않습니다.
// 따라서, HTMLCollection 또는 NodeList를 그대로 사용할 때는 부작용 예방 차원 및 고차 함수 지원을 위해 Array 로 치환해 사용할 것을 권장합니다.
const $fruits = document.querySelectorAll(".red");
const fruits = Array.from($fruits)
fruits.forEach(fruitDom => fruitDom.className = "blue")

//## 객체를 만드는 방법 
//1. 모형없이 만들 때 1-1 new Object / 1-2 JSON ==> 관련사항을 그냥 묶기만 하는 것 
//*JSON (JavaScript Object Notation 자바스크립트 객체 표기법) : 다른 언어에서는 Json이 문자열이다. JS에서는 객체이기 때문에 서버에게 전달하려면 문자열로 변환하여 전달
//문자열변환 let a = JSON.stringify(객체명)
//객체 변환 let b = JSON.parse(문자열명) : 서버에서 넘어오는 json 타입이 string이다. 따라서 객체로 변환하여 사용한다.
//2. 모형준비 만들 때 2-1 생성자함수 / 2-2 클래스 
//객체 순환 for in 문을 쓸 때 주의점 => user[key] 으로만 사용가능 
let user = {
    name: 'kim',
}
for(let key in user) {
    console.log(user.key, user[key], key) // undifined, kim, name ==> user.key 는 user.'key'으로 해석되기 때문
}
//for of, for in 차이
// for(let i in user) ==> i는 프로퍼티명 즉 키, name => 객체 순환 시 사용
// for(let i of user) ==> i는 값 즉 인덱스가 아닌 값 => 배열(유사배열) 순환 시 사용, 배열에서 for in을 사용하면 i는 인덱스가 된다.
// forEach는 배열만을 위한 함수

//## this : 현재 함수를 호출한 객체 자신을 지칭하는 예약어, 실행시점에 this가 결정


//xml : eXtensible Markup Languge 

//동기 : 순차적 진행, 비동기 : 병렬 진행 

//## AJaX : Asynchronous Javascript + XML
// 웹 어플리케이션 개발시에 클라이언트와 서버의 통신방법에 대한 형태로 자바스크립트와 XML에 기반한 비동기 통신기법을 사용함. 
//즉, 자바스크립트로 HTTP요청을 보내고 XML로 응답을 받아서 처리하는 개발방식.
//1. ajax 준비
let xhr = new XMLHttpRequest()
//2. 서버요청 정보설정
xhr.open('get', api키값포함유알엘, true)
//3. 요청 보낸다.
xhr.send()
//4. 응답 결과를 받을 콜백함수 지정
xhr.addEventListener('load', function(){
    let result = xhr.responseText 
    result = JSON.parse(result)
})

//지도링크 https://google.co.kr/maps/@위도,경도,16z 
