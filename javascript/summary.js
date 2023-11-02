//## window.onload
//DOM Node가 #a1을 메모리에 할당한 후에 실행해라. window는 브라우저를 지칭, onload : 브라우저가 html 파싱이 완료된 순간임 즉 메모리할당이 끝난 순간. 즉 일반적으로 돔노드를 접근하는 코드는 온로드 이벤트 안에 작성함
window.onload = function(){ 
        let heading = document.querySelector("#a1")
        heading.onclick = function(){
            heading.style.color = 'blue'
        }
}

//## 후행,선행 연산
a = 10
b = a++ //b=10, a=11 후행연산
b = ++a //b=12, a=12 //선행연산


//#호이스팅(JS에서만 허용) ==> 그래서 let을 사용함.
a = 9 
console.log(a)  //9 => var a 가 호이스팅 되어서 a는 인식하지만, 값의 호이스팅까지는 일어나지않음
var a = 10      // 값은 여기와서 다시 대입된다.
console.log(a)   // 10
console.log(a+b)  //NaN => 10 + undefined
var b = 20        
console.log(a+b) //30 


//var : 호이스팅O, 중복선언O, 함수스코프만 지원, 다른 블록스코프들은(if,for) 스코프를 지원하지않음
//let : 호이스팅 X, 중복선언X, 함수,if,for 등 블록스코프 지원
// Heap, Stack 메모리 : 각각의 저장 공간이 다름, 따라서 변수명이 같아도 다른 저장공간에 저장됨으로 에러가 나지 않음 
let name = "힙" //전역변수는 Heap 메모리에 저장
function myFunc(){
    let name = "스택" //지역변수는 Stack 메모리에 저장  
    console.log(name)
}
myFunc() //스택
console.log(name) //힙


//## 함수 표현식
//즉시실행함수 : 선언과 동시에 호출
(function (매개변수) {
    // statements
})()

//일반함수 : function 예약어, func 식별자
function func(매개변수){ 
    //함수body
}

//익명함수 : 식별자가 없는 함수, 매개변수로 함수를 전달할 때 사용할 수 있음.
let sum = function(par1,par2) {
    return par1+par2
}
sum(10,20)

//화살표함수 : 익명함수의 축약형으로 볼 수 있다. 파이썬에서는 Lambda 함수라고 부름 
//(매개변수) => { 함수body } : 매개변수 1개일 경우 () 생략가능, 함수body가 한줄이고 return문이라면 {} 생략가능, para => a + b
let myFunc1 = (no1, no2) => no1 + no2 
myFunc1(10,20)
//hof(high order function)에서 주로 사용 : 다른함수를 매개변수로 받아들이는 함수, 함수를 결과로 리턴하는 함수


//## 객체 : 관련된 변수,함수를 묶은 것 

