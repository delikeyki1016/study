const express = require('express')
const morgan = require('morgan')

const app = express()
app.set('port', process.env.PORT || 3000)

app.use(morgan('dev'))

//forward 방식 : 클라이언트 요청을 다른 url 요청으로 돌린다. backend에서 다른 url의 미들웨어가 실행되게 처리, req, res 각 1번 발생
// 클라이언트 브라우저의 url이 바뀌지는 않는다. 
// 여러 미들웨어를 실행시킬 수 있지만, send()는 한번만 실행해야한다.
app.get('/one', (req, res, next) => {
    // 업무처리 후 다른 url의 미들웨어가 실행되게 한다.
    // 클라이언트 요청 url을 변경시키고 next()
    req.url = '/two'
    // 데이터 전달도 가능
    res.locals.data1 = 'hello'
    next()
})

app.get('/two', (req, res) => {
    let data = res.locals.data1
    res.send(`I am too middleware, ${data}`)
})

//redirect 방식 : 클라이언트 요청을 다른 url 요청으로 돌린다. 응답해서 브라우저가 자동으로 다른 url로 요청, req, res 각 2번 발생
// 브라우저의 url은 변경된다. 응답이 2번 발생하기때문에 각각 send()해도 무방함 
app.get('/three', (req, res) => {
    // 브라우저에게 명령 
    res.redirect('/four')
})

app.get('/four', (req, res) => {
    res.send(`I am four middleware`)
})



app.listen(app.get('port'), ()=> {
    console.log(app.get('port'), '번 포트로 대기중')
})