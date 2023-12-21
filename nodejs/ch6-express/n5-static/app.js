// static 미들웨어 : express에서 제공
// 인수로 정적파일의 경로를 제공, fs.readFile로 직접 읽어올 필요가 없음, 
// 요청하는 파일이 없으면 알아서 next를 호출해 다음 미들웨어로 넘어감
// 요청하는 파일이 있으면 다음 미들웨어는 실행되지 않음 
// 선언순서는 보통 morgan - static ~~~ 에러처리(마지막)

const express = require('express')
const path = require('path')
const morgan = require('morgan')

const app = express()
app.set('port', process.env.PORT || 3000)

// 미들웨어는 등록순서가 중요 
app.use(morgan('dev')) 
// static은 next() 호출하지 않음 
// app.use(express.static(path.join(__dirname, 'public'))) // __dirname : 해당앱이 실행되고 있는 폴더

// url 경로와 서버 경로를 바꾸려면(보안 상 좋음)
app.use('/static', express.static(path.join(__dirname, 'public')))
// http://localhost:3000/static/index.html 로 접속하면 성공 

app.get('/', (req, res)=>{
    res.send('router 응답')
})

app.get('/dynamic', (req, res)=>{
    res.send('dynamic 응답')
})

app.listen(app.get('port'), ()=> {
    console.log(app.get('port'), '번 포트로 대기중')
})
