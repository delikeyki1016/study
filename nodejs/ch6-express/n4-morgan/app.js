// morgan : 서버로 들어온 요청,응답을 자동으로 기록해주는 미들웨어 (별도설치 필요 npm i morgan)
// 로그의 정보량 선택 가능(dev(개발 시), tiny, short, common, combined(운용로그))
// 운용로그(에러,중요이벤트 등..)는 보통 영속적으로 저장함(보통 파일로 저장함) ==> 감사 시 필요
// 보통 맨 위에 등록해둠 

const express = require('express')
const morgan = require('morgan')
const fs = require('fs')

const app = express()
app.set('port', process.env.PORT || 3000)

// morgan 등록
// app.use(morgan('dev')) 
// GET / 304 2.161 ms - - => GET방식, url : / , 상태코드, 걸린 시간, 전달된 데이타용량

// app.use(morgan('combined'))
// ::1 - - [19/Dec/2023:05:48:08 +0000] "GET / HTTP/1.1" 304 - "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
// ip어드레스, 요청날짜, get방식/프로토콜, 상태코드, 클라이언트 유저 에이전트

// 운용로그 파일 저장하기
const accessLogStream = fs.createWriteStream(
    `${__dirname}/../log/access.log`,
    {flags:'a'} // append 요청
)
// 우리가 만든 file stream을 morgan에 연결
app.use(morgan('combined', {stream: accessLogStream}))

app.get('/', (req, res) => {
    res.send('morgan test...')
})

app.listen(app.get('port'), ()=> {
    console.log(app.get('port'), '번 포트로 대기중')
})