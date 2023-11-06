//## window.onload : HTML/xml 파서가 문서를 파싱해서 DOM node객체가 생성되면서 DOM Tree를 만든 후에(JS메모리에 저장) 실행해라 
//즉 DOM node로 접근하는 스크립트는 window.onload안에서 작성해야 한다.
window.onload = function () {
    let a = document.querySelector("#a1")
    //실행
};
//window 객체의 계층구조 
//브라우저 자식들 : window, document, navigator, history, location
//window 객체의 프로퍼티들 : innerWidth,innerHeight,localStorage,sessionStorage,scrollX,scrollY,parent(팝업을 호출한 부모브라우저, 또는 iframe의 상위html)
//window 객체의 메서드 : alert,confirm,prompt,stop(load 멈추기),open,onload 
//history 객체 : back, forward, go(-2) 전전페이지로 이동
//location 객체 : href, host, hostname, hash, pathname, port, protocol, search(쿼리값)


//## 후행,선행 연산
a = 10;
b = a++; //b=10, a=11 후행연산
b = ++a; //b=12, a=12 //선행연산

//##호이스팅(JS에서만 허용, 게양, 위로 끌어올려짐) ==> 그래서 let을 사용함.
a = 9;
console.log(a); //9 => var a 가 호이스팅 되어서 a는 인식하지만, 값의 호이스팅까지는 일어나지않음
var a = 10; // 값은 여기와서 다시 대입된다.
console.log(a); // 10
console.log(a + b); //NaN => 10 + undefined
var b = 20;
console.log(a + b); //30

// 매개변수(parameter) : 함수선언 시 데이터를 전달받기 위한 변수
// 인수(argument) : 함수 호출시 매개변수에 넘겨주는 값

// string은 유사배열로써, index와 length를 가진다. 재할당(주소변경)은 가능하나, 변수[0] = "변경값"을 지정할 순 없다.

//var : 호이스팅O, 중복선언O, 함수스코프만 지원, 다른 블록스코프들은(if,for) 스코프를 지원하지않음
//let,const : 호이스팅 X, 중복선언X, 함수,if,for 등 블록스코프 지원
// let, const로 선언한 전역변수는 window객체의 프로퍼티가 아니다. 
// ex) let foo = 1 => window.foo (X) var선언은 window객체의 프로퍼티이다. 

// const는 선언과 동시에 초기화(할당)이 되어야 함(재할당 금지), 일반적으로 상수는 대문자로 선언하고 언더스코어로 구분(스네이크) ex) const TAX_RATE = 0.1

// const로 객체를 선언한 경우는 프로퍼티 키값을 변경할 수 있다. 
const person = { name: 'lee' } 
person.name = 'Kim'
console.log(person) // {name:'Kim'}

// 재할당이 필요한 경우 let을 사용하고 최대한 스코프를 좁게 만들어야 한다. 

// Heap, Stack 메모리 : 각각의 저장 공간이 다름, 따라서 변수명이 같아도 위치에 따라 저장공간이 분리됨으로 에러가 나지 않음
// Heap : 어플리케이션이 구동되는 동안 사용되는 메모리, 전역변수 저장
// Stack : 함수 실행시 사용되는 메모리, 함수 종료 시 함수 관련 지역변수들은 제거됨
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

//익명함수 : 식별자가 없는 함수, 매개변수로 함수를 전달할 때 사용할 수 있음.
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

//## 객체 : 관련된 변수(프로퍼티),함수(메소드)를 묶은 것, 프로그램에서 인식할 수 있는 모든 대상
// instance (사전적의미:사례) : 객체는 new 키워드를 통해 Date객체의 인스턴스를 만들어 변수에 저장하여 사용한다.
let now = new Date() // Date 내장객체의 인스턴스를 만들어서 now 변수에 저장 
now.toLocaleString() // .은 객체의 멤버접근연산자. Date객체의 toLocaleString메서드를 사용
let dateSet = new Date(2023, 10, 3, 17, 3, 24, 0) //시간을 셋팅해서 생성할때 월은 11로 떨어진다. 0~11의 숫자로 월을 표시하므로 11은 12월임. 월 사용시 -1이 필요.

//property : 객체의 속성
//method : 객체의 동작, 함수와 같은 역할을 하기때문에 ()붙여야 함. ex)now.toLocaleString()

let array = new Array() //Array 클래스로 array 객체를 생성
let array1 = ['사과','포도','딸기']
array1.forEach((elements) => { //forEach는 매개변수에 함수전달. 배열의 elements갯수만큼 함수를 호출
    console.log(elements)
})
console.log(typeof array1) //object
console.log(array1 instanceof Array) //왼쪽의 객체가 오른쪽의 객체(클래스)로 만든것이냐, true/false 반환

//##Array 객체의 메서드
//every : 배열요소가 주어진 조건에 대해 참이면 true, 거짓이면 false 
let array2 = [1,2,3,4,5]
let result2 = array2.every(element => element > 0) //true
//filter : 조건에 대해 참인 것만 골라 새로운 배열을 만듦 array2.filter((element) => 조건)
//forEach : 배열요소에 대해 매개변수로 넣은 함수를 실행
//map : 함수 결과를 모아서 반환
let result3 = array2.map((element) => element * 2)
console.log(result3) //[2,4,6,8,10]
//indexOf : 조건에 일치하는 첫 index를 반환
//push : 끝에 추가, unshift : 앞에 추가
//pop : 끝을 반환, shift : [0]을 반환
//splice(index, 삭제할갯수, 추가할데이타) : splice(2) 2부터~마지막까지 삭제, splice(2,1) 2부터 1개만 삭제, splice(2,1,"js") 2부터 1개를 삭제하고 그자리에 "js"를 추가(즉 수정)
//slice : 추출만 하고, 원본배열은 변하지 않음, slice(2) 2부터 마지막까지 추출, slice() 전체 복사 추출
let result4 = array2.slice(2,4) //index 2부터 index3까지 추출
console.log(result4)
//sort : 정렬 
//toString : 문자열로 반환, ,로 구분해줌

//##Math 객체의 메서드 : Math는 인스턴스 생성없이 사용할 수 있다.
//cell() 소수점 이하를 올림
//floor() 소수점 이하를 버림
//round() 소수점 이하를 반올림
//random() 0~1 소수값 추출, 0~100 사이의 랜덤 => Math.floor(Math.random() * 100) / 1~9사이랜덤 Math.random() * (10-1) + 1
//max(), min() 큰수, 작은수

// ##DOM 
//document.querySelectorAll("ul li") ==> 배열로 반환 
//pageX(스크롤 포함), clientX(스크롤 미포함), screenX(브라우저탭부분까지 포함)
//addEventListener(이벤트, 함수, 캡처 여부) : 캡처여부는 기본이 false(버블링), true(캡처링) / onclick 이벤트함수는 캡처여부를 핸들링할수X
//<div id="부모" onclick="함수"><div id="자식" onclick="함수"></div></div>
//버블링 : node가 중첩되었을 때 자식에게 클릭이벤트가 발생될 때 부모에게도 클릭이벤트가 발생된다.  event.stopPropagation() //propagation:번식, 버블링을 막음
//캡처링 : 이벤트가 부모에서 자식으로 내려옴
//event.target(실제 이벤트가 발생한 타겟), event.currentTarget(이벤트를 등록한 타겟, a.addEventListener라면 a를 지칭)
//true(캡처링) div1 - div2 - div3 의 순서대로 이벤트 처리
//false(버블링)=> 이게 기본값 div3 - div2 - div1 의 순서대로 이벤트 처리
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
    // event.stopPropagation() //propagation:번식, 버블링을 막음
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
pAtt.value = 'color:red'
addP.setAttributeNode(pAtt)
let pText = document.createTextNode("텍스트추가")
addP.appendChild(pText)
div.appendChild(addP)


//노드 삭제
//1. 삭제할 노드의 부모노드 선택 => let node = 삭제할노드.parentNode
//2. 부모노드.removeChild(삭제할노드) => node.removeChild(삭제할노드)
document.getElementById('deleteNode').addEventListener('click', function(){
    document.getElementById("nodetest").removeChild(addP)
})