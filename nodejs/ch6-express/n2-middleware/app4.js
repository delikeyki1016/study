const express = require('express')

const app = express()
app.set('port', process.env.PORT || 3000)

// 미들웨어 1, get 라우터
app.get('/', (req, res) => {
    res.send('/.. hello express')
})

// 서버 오류 상황 미들웨어2
app.get('/test/:no', (req, res) => {
    let no = req.params.no 
    if(no > 10){
        res.send(`정상적인 상황, 당신이 입력한 숫자는 ${no} 입니다.`)
    } else {
        // 특정 상황을 에러 상황으로 만들기 => throw new Error(에러메시지)
        throw new Error('서버오류... 에러코드 111, 관리자에게 문의')
    }
})

// 미들웨어 3
app.get('/test2/:no', (req, res, next) => {
    let no = req.params.no 
    if(no > 10){
        res.send(`정상적인 상황, 당신이 입력한 숫자는 ${no} 입니다.`)
    } else {
        // next()함수에 매개변수를 지정하면 에러메시지
        next('서버오류... 에러코드 222, 관리자에게 문의')
    }
})


// 미들웨어 4, 위의 조건이 아닌 경우 설정(404) => 요청이 잘못되었을 때 실행되는 미들웨어는 가장 마지막에 등록하는 것이 일반적
app.use((req, res, next) => {
    // res.send()는 status code 200 
    // 404 이지만 send로 메시지를 알려줌 
    res.status(404).send('요청하신 파일이 없습니다. url 확인해주세요')
})

// 에러처리 미들웨어 5, 일반적으로 가장 아래부분에 작성
app.use((err, req, res, next) => {
    console.log('err내용:', err)
    // 보통 서버오류는 500으로 넘겨야 하지만, 해킹 방지차원으로 정상상황인 것처럼 200으로 넘기기도 한다. 
    res.send('에러가 발생했습니다.')
})


app.listen(app.get('port'), ()=> {
    console.log(app.get('port'), '번 포트로 대기중')
})