const express = require('express')

const app = express()
app.set('port', process.env.PORT || 3000) // set은 어플리케이션 내에서 공유가능함

// 미들웨어 간의 데이터 전달 res.locals
// data 유지
// 모든 유저의 모든 요청 app 
// 한 유저의 모든 요청 session
// 한 유저의 한번 요청시 req, res 

// 미들웨어 등록, 실행 순서 테스트, 등록된 순서대로 실행
// 미들웨어 등록 함수는 use()이지만, 
// get,post 등의 http request method에 의해 실행될 미들웨어를 조금 더 편하게 등록하기 위해 get(), post()등의 함수를 제공함(라우터)
// 미들웨어는 개발자 함수
// 아래처럼 get,post 등의 함수로 등록하는 미들웨어를 "라우터"라고 부른다.
// 미들웨어 1 
app.post('/', (req, res) => { // '/' 경로조건이 추가되면 제일 먼저 실행이 안될 수도 있다. 
    res.send('post... hello express')
})
// 미들웨어 2
app.get('/', (req, res) => {
    res.send('get... hello express')
})

// 개발자 함수가 미들웨어이다.
// (req, res) => {
//    res.send('get... hello express')
//}

// 미들웨어 3 
// get,post로 미들웨어를 등록하면서 next()를 할 수도 있긴 하지만, 일반적으로는 최종 처리 개념의 코드가 등록되기때문에 next() 호출을 잘 안한다.
// 동일조건으로 여러개의 미들웨어가 실행된다면 범위가 좁은 미들웨어를 위에 선언하는 것이 좋다.
app.get('/user/park', (req, res, next) => {
    res.send('user/park...')
    // 아래의 경우는 에러발생, 미들웨어에서 다음 미들웨어를 실행시키기 위해서 사용하는 함수는 next()
    // next()
    // app.use(), app.get()에서 next()를 사용할 수도 있지만, 보통의 경우 app.use() 로 등록하는 미들웨어는 여러 요청시 공통으로 실행될 로직이기때문에
    // 공통 부분이 실행되고 그 다음 미들웨어가 실행되게 next()를 활용한다.
    // app.get(), app.post()들은 라우터이기 때문에 유저 요청시 유저화면이 조정되는 결과를 전송하는 역할이기 때문에
    // next()에 의해 여러 미들웨어를 실행할 순 있지만, res.send를 한번 한 이후에는 커넥션이 끊어지기 때문에 연이어 res.send 할 수 없다. (그래서 에러남)
    // 결론 app.get(), app.post() 등..과 같은 라우터는 next()를 잘안쓴다.
    // next를 호출해야 다음 코드로 넘어감 
})

// 미들웨어 4
// url경로에 :xxx 는 임의 단어(dynamic url) :aaa라면 req.params.aaa
app.get('/user/:name', (req, res) => {
    res.send(`user/:name...  ${req.params.name}`)
})

// 미들웨어 5
app.get('*', (req, res) => {
    res.send('*...')
})



app.listen(app.get('port'), ()=> {
    console.log(app.get('port'), '번 포트로 대기중')
})