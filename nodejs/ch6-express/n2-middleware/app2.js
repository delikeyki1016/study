const express = require('express')

const app = express()
app.set('port', process.env.PORT || 3000)

// 미들웨어 실행 순서 테스트
// 미들웨어 1, use : 미들웨어를 등록하는 함수 
app.use((req, res, next) => {
    console.log('middleware 1, before next()')
    next()
    console.log('middleware 1, after next()')
})

// 미들웨어 2
app.use((req, res, next) => {
    console.log('middleware 2, before next()')
    next()
    console.log('middleware 2, after next()')
})

app.get('/', (req, res)=>{
    res.send('get... /')
})

app.get('/about', (req, res)=>{
    res.send('get... /about')
})

// 미들웨어 3
app.use((req, res, next) => {
    console.log('middleware 3, before next()')
    next()
    console.log('middleware 3, after next()')
})



app.listen(app.get('port'), ()=> {
    console.log(app.get('port'), '번 포트로 대기중')
})