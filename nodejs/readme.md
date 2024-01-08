* backend web application : 항상 실행상태, port 점유, 요청 대기 
* 요청분석 - 요구 실행 - 결과 리턴 

* 라이브러리 : 내 코드 내에서 원하는 시점에 해당 기능을 갖다 씀
* 프레임워크 : 만들어진 구조위에서 개발
* 백엔드 프레임워크들 : java - spring boot / JS - node express / python - django / .net - asp.net 

## node.js
* node.js는 크롬v8자바스크립트 엔진으로 빌드된 ***자바스크립트 런타이머***(브라우저와 html 종속성을 제거하고 독립적으로 실행)
* *런타임 : 특정 언어로 만든 프로그램을 실행할 수 있게 해주는 가상 머신

* Blocking : 동기적 실행, 함수를 콜한 메인쪽에서 콜된 함수실행이 완료될 때까지 대기(블록킹)함. 코드진행이 한 줄로 이어짐 
* Non-Blocking : 비동기적 실행, 시간이 오래 걸리면서 동시 진행이 가능한 업무에 해당 : Input/Output(file Read/Write, Networking), 암호화, 압축

* OS -> process 구동 -> main thread 생성 -> code 실행 
* process : application 실행 단위
* thread : code 실행 단위
* 노드 프로세스는 멀티스레드이지만(4개) 직접 다룰 수 있는 스레드는 하나이기 때문에 싱글스레드라고 표현. 14버전 부터 멀티스레드 사용가능(그러나 복잡도때문에 사용하진않음)
* 싱글스레드 : 주어진 일을 하나밖에 처리하지 못함.(비효율)
* 노드는 일부 코드를(I/O) 백그라운드(다른 프로세스)에서 실행함 
* ***즉 노드는 Event기반, Single Thread Model, Non-blocking IO 제공***

* *20.10.0 LTS : Long Term Service version
* 환경변수 - path설정은 OS의 어느 디렉토리 위치에서나 실행가능하도록 설정

## module
* JS에서는 모듈이 JS파일
```
exports.xxx(외부 노출 이름) = yyy(파일 내의 이름)
```
```
module.exports = {  //json으로 export
    data,
    myFun33: myFun3, //myFun33 키값을 따로 지정할 수도 있다.
    MyClass3
}
```
```
const {data: data33, myFun33, MyClass3} = require('./module3')  // 따로 따로 받거나,
const module3 = require('./module3') //객체로 받을 수 있다.
```
## 노드 내장 객체
* global : 전역객체, 생략가능 ex) global.console.log (자바스크립트에서의 window.console.log 와 같은 개념)
* console.trace : 호출스택 로깅 
* console.time, console.timeEnd : 시간 로깅 (time ~code~ timeEnd : code가 걸리는 시간측정)
* process.nextTick, promise : setTimeout, setInterval보다 우선순위가 높아서 백그라운드에서 먼저 실행됨 

## 노드 내장 모듈
* path : path.sep (경로 구분자 윈도우\), path.dirname(파일의 폴더경로), path.extname(파일 확장자), path.basename(파일이름,확장자포함), path.parse(파일경로를 root,dir,base,ext,name으로 분리), path.isAbsolute(파일경로가 절대경로인지 상대경로인지 true,false로 알려줌)
* url : url정보를 항목별로 구분할 수 있음(protocol, username, password, host, pathname, query(key=value&), hash) protocol~port:origin
* createHash : 단방향 암호화 (비밀번호 => createHash, 해시문자열이 같은지 다른지만 판별) 
* 양방향 암호화 : 암호화 crypto.createCipheriv(알고리즘, 키, iv) / 복호화 crypto.createDecipheriv(알고리즘, 키, iv)

## HTTP 모듈로 서버 만들기


## REST API 
* API (Application Programming Interface) : 어플리케이션에서 데이터를 읽거나 쓰기 위한 인터페이스
  - ex)서울시 공공데이터 Open API (public API)
* REST (Representational State Transfer : 대표 상태 이전) 
  - 클라이언트와 서버간의 통신방식, 인터넷식별자 URI(Uniform Resource Idenfifier)와 http를 이용한 통신 유형(data만을 전송)
  - http프로토콜을 이용해서 client에게 request를 받으면, response에 http request method 방식에 따라 data를(json,xml) 전송 
* RESTful : REST가 적용된 시스템
* http request method : request header에 method 지정(GET 조회(기본값), POST 등록, PUT 수정, PATCH 일부 수정, DELETE 삭제)

* GET 방식 : body없음, POST 방식 : body에 데이타 전달 

## cookie (client side), session (server side) : http 상태 유지 기법
http 프로토콜: 
- connection oriented
- stateless : 프로토콜 자체에서 상태 유지X, request 1 - response 1 가 완료되면 해당 connection을 종료함으로 서버 부하를 줄임
단점은 connection 정보로 유저 히스토리(로그인, 장바구니, id기억하기체크)를 유지할 수 없다. ==> 그래서 유저의 상태를 cookie나 session 활용하여 저장해둠

* cookie : response header에 쿠키 정보를 담아 응답하고 브라우저가 쿠키데이타를 expired 기한에 따라 브라우저 메모리에 담음, 이후 해당 사이트에 방문시에 request header에 해당 쿠키를 담아 요청하면 request에서 쿠키 추출.

* session : 보안 상 민감한 상태 데이터의 경우는 클라이언트를 식별하여(쿠키) 서버사이드 세션에 저장함.(식별자와 값으로 저장) 식별자를 쿠키에 담아 클라이언트에 전송함. 

## package.json : npm 환경파일 
* npm run test : test는 package.json내 scripts에 등록된 스크립트 명, 자주쓰는 명령어를 등록해서 사용한다.
* npm i -g express cookie-parser : 글로벌로 설치하면 C:\Users\사용자명\AppData\Roaming\npm\node_modules 에 설치된다. 프로젝트마다 버전관리를 따로 하기때문에 글로벌 설치는 권장사항은 아니다. (글로벌삭제도 -g 붙여서 npm uninstall -g express)
* npm i -D nodemon : (-D : 개발시에만 필요한 툴로써 사용하는 모듈일 경우, --save-dev 같음) devDependencies에 등록됨
package.json scripts에 등록해서 사용가능(실행 npm start)
```
"scripts": {
    "start": "npx nodemon app1.js"
  },
```
* 전달받은 package.json이 있으면 해당 파일이 있는 곳에서 npm install (package.json 선언되있는 패키지가 해당 버전으로 자동 설치)
* "express": "^4.18.2" => major 버전을 제외한 minor, patch 버전은 업그레이드 되어도 무관함. (@latest 최신버전) "~4.18.2" patch 만 업그레이드 
* npm outdated : 패키지에 버전 변화를 볼 수 있다.
* nodemon : 소스 수정&저장 시 자동으로 서버 재시작해줌(hot deploy)
* npx : 
* middleware : request - middleware - response (express는 미들웨어의 조합), 등록순서가 실행순서

## 템플릿 : 동적데이터를 어떤 문서에 삽입하여 html로 랜더링되어 응답될 때, 해당 문서가 템플릿
* res.render(뷰, 데이터) => 뷰: 템플릿명, 뷰에 데이터를 삽입하여 html로 렌더링해라 
* 템플릿엔진 : Pug, Nunjucks

## 시퀄라이즈 ORM(Object Relational Mapping) 
- 시퀄라이즈 : SQL 작업을 쉽게 할 수 있도록 도와주는 라이브러리
- ORM : 객체와 데이터를 매핑해줌
- sequelize, sequelize-cli 설치, npx sequelize init (시퀄라이즈 구조 생성) 
*cli : Command Line Interface
