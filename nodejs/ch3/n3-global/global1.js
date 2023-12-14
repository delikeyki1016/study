// 앱 전역에서 사용할 수 있는 변수, 함수, 클래스 등록
// require 없이 사용 가능
// JS에서의 window. 의 전역객체와 같다. 노드는 global. 전역객체 
global.message = 'hello'

function sayHello(){
    console.log(global.message)
}

module.exports = {
    sayHello
}