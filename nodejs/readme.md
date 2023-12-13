* backend web application : 항상 실행상태, port 점유, 요청 대기 
* 요청분석 - 요구 실행 - 결과 리턴 

* 라이브러리 : 내 코드 내에서 원하는 시점에 해당 기능을 갖다 씀
* 프레임워크 : 만들어진 구조위에서 개발
* 백엔드 프레임워크들 : java - spring boot / JS - node express / phthon - django / .net - asp.net 

## node.js
* node.js는 크롬v8자바스크립트 엔진으로 빌드된 자바스크립트 런타이머(브라우저와 html 종속성을 제거하고 독립적으로 실행)
* *런타임 : 특정 언어로 만든 프로그램을 실행할 수 있게 해주는 가상 머신

* Blocking : 동기적 실행, 함수를 콜한 메인쪽에서 콜된 함수실행이 완료될 때까지 대기(블록킹)함. 코드진행이 한 줄로 이어짐 
* Non-Blocking : 비동기적 실행, 시간이 오래 걸리면서 동시 진행이 가능한 업무에 해당 : Input/Output(file Read/Write, Networking), 암호화, 압축
* *node는 기본적으로 I/O같은 업무를 논블로킹으로 진행한다.

* OS -> process 구동 -> main thread 생성 -> code 실행 
* process : application 실행 단위
* thread : code 실행 단위
* 노드 프로세스는 멀티스레드이지만(4개) 직접 다룰 수 있는 스레드는 하나이기 때문에 싱글스레드라고 표현. 14버전 부터 멀티스레드 사용가능(그러나 복잡도때문에 사용하진않음)
* 싱글스레드 : 주어진 일을 하나밖에 처리하지 못함.(비효율)
* 노드는 일부 코드를(I/O) 백그라운드(다른 프로세스)에서 실행함 

* *20.10.0 LTS : Long Term Service version
* 환경변수 - path설정은 OS의 어느 디렉토리 위치에서나 실행가능하도록 설정

## module
* JS에서는 모듈이 JS파일
* exports.xxx(외부 노출 이름) = yyy(파일 내의 이름)
* module.exports = { => json으로 export
    data,
    myFun33: myFun3, => myFun33 키값을 따로 지정할 수도 있다.
    MyClass3
}
* const {data: data33, myFun33, MyClass3} = require('./module3') => 따로 따로 받거나,
* const module3 = require('./module3') => 객체로 받을 수 있다.
