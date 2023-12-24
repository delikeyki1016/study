// body-parser (express 자체 지원)
// GET : url 뒤에 ?name1=value1&name2=value2 방식으로 request header에 해당url을 담아 전달 
// POST, PUT : 클라이언트 데이터를 request body에 추가해서 전달 or 개발자코드에서 ajax data 전송 시에 => body parser 이용 

// multer 패키지 : 파일업로드 미들웨어

const express = require('express')
const morgan = require('morgan')
const path = require('path')

const app = express()
app.set('port', process.env.PORT || 3000)

app.use(morgan('dev'))
app.use(express.static(path.join(__dirname, 'public'))) // 정적파일을 알아서 호출해줌 

// test 1 : param 데이터(클라이언트 요청 url의 path값 추출)
// path 부분에 데이터를 받고자 하는 곳에 :xxx (:임의 단어로 임시 변수로 사용가능)
// /kim/seoul/10
app.get('/:name/:addr/:age', (req, res) => {
    res.send(`param test1: ${req.params.name}, ${req.params.addr}, ${req.params.age}`)
})
// /name/kim/data/10
app.get('/name/:name/data/:data', (req, res) => {
    res.send(`param test2: ${req.params.name}, ${req.params.data}`)
})

// test 2 : query(search) 문자열 획득, request header에 담아 전달
// /query1?name=kim&addr=seoul&age=10 
app.get('/query1', (req, res) => {
    res.send(`query1 test: name=${req.query.name}, addr=${req.query.addr}, age=${req.query.age}`)
})

// 체크박스나 멀티플에서 다중 선택이 된 경우는
// /query2?name=soran&apple=apple&peach=peach&ide=vscode&ide=eclipse&language=HTML&cars1=Audi&cars2=Volvo&cars2=Audi
app.get('/query2', (req, res) => {
    let ide = req.query.ide
    console.dir(ide)
    let ideResult = ''
    if (ide && Array.isArray(ide)){ // ide 값이 있고, 다중 선택한 경우 
        ide.forEach((element) => {
            ideResult += element + ','
        })
    } else { // 한개 선택한 경우
        ideResult = ide
    }

    let car2 = req.query.cars2
    let car2Result = ''
    if (car2 && Array.isArray(car2)){  
        car2.forEach((element) => {
            car2Result += element + ','
        })
    } else {
        car2Result = car2
    }   
    res.send(`query2 test:
        입력하신 데이터는 
        name=${req.query.name}, apple=${req.query.apple}, peach=${req.query.peach}, 
        ide=${ideResult},
        language=${req.query.language}, car1=${req.query.cars1}, 
        car2=${car2Result}`)
})

// test 3 form body
// post 방식이면 request body에 전달됨
// express.urlencoded : 이 미들웨어 함수는 HTTP POST 요청의 본문(body)에 인코딩된 데이터를 해석하고, req.body 객체에 채워넣어주는 역할
// extended 옵션, express의 바디 파서가 내부적으로 이용하는 모듈이 여러개 준비되어있는데, QS라는 모듈을 이용해서 파싱해라 (거의 대부분이 QS 이용)
// 요청헤더의 컨텐츠 타입이 Content-Type:application/x-www-form-urlencoded
// application/x-www-form-urlencoded 인코딩 방식이란? 데이터를 "key: value" 와 같은 형태로 만들어 주는 방식 
app.use(express.urlencoded({extended: true})) // false : querystring 모듈 사용
app.post('/form', (req, res) => {
    console.log('바디', req.body)
    let ide = req.body.ide 
    console.dir(ide)
    let ideResult = ''
    if (ide && Array.isArray(ide)){ 
        ide.forEach((element) => {
            ideResult += element + ','
        })
    } else { 
        ideResult = ide
    }

    let car2 = req.body.cars2
    let car2Result = ''
    if (car2 && Array.isArray(car2)){  
        car2.forEach((element) => {
            car2Result += element + ','
        })
    } else {
        car2Result = car2
    }   
    res.send(`form test:
        입력하신 데이터는 
        name=${req.body.name}, apple=${req.body.apple}, peach=${req.body.peach}, 
        ide=${ideResult},
        language=${req.body.language}, car1=${req.body.cars1}, 
        car2=${car2Result}`)
})


// test 4 : ajax json 데이터
// json 미들웨어 (express 제공)
// js에서 json은 객체이고 네트워크 전송 시에는 문자열
// json.parse(문자열), json.stringify() 해줘야하는데, express에서 알아서 변형해줌 
// 요청헤더의 Content-Type: application/json
app.use(express.json())
app.post('/json1', (req, res) => {
    res.send(`json data: name=${req.body.name}, score=${req.body.score}`)
})

// test 5 : ajax 일반 문자열
// 요청헤더 Content-Type: text/plain;charset=UTF-8
const bodyParser = require('body-parser')
app.use(bodyParser.text())//일반 문자열이다.. 
app.post('/string1', (req, res) => {
    console.log('바디파서', bodyParser.text())
    res.send(`string data : ${req.body}`)
})

app.listen(app.get('port'), ()=> {
    console.log(app.get('port'), '번 포트로 대기중')
})