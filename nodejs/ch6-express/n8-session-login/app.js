// npm i express-session

const express = require('express')
const morgan = require('morgan')
const cookieParser = require('cookie-parser')
const session = require('express-session')

const app = express()
app.set('port', process.env.PORT || 3000)

app.use(morgan('dev'))
app.use(cookieParser('secret@1234')) // 암호화된 쿠키를 사용하기 위한 임의 문자열(key), 보안을 위한다면 dotenv로 빼서 사용하는것이 좋다.
app.use(session({
    secret: 'secret@1234',
    resave: false,
    saveUninitialized: true, // 유저가 처음 접속했을 때 메모리를 할당해줄까?
    cookie: {
        httpOnly: true, // front js 에서는 이 쿠키데이터를 접근하지 못하게 함
    }
})) 
// app.use(express.json())
app.use(express.urlencoded({extended: true}))

app.get('/', (req, res) => {
    if(req.session.loginId) {
        //로그인한 유저.. 
        const output = `
            <h2>로그인한 사용자</h2>
            <p>${req.session.loginId}님 환영합니다.</p>
        `
        res.send(output)
    } else { // 로그인하지 않았던 유저라면,
        const output = `
            <h2>로그인하지 않았습니다.</h2>
            <form action='login' method='post'>
                ID: <input type="text" name="id" /><br />
                Password: <input type="text" name="pw" /><br />
                <button type="submit">로그인</button>
            </form>
        `
        res.send(output)
    }
})

app.post('/login', (req, res)=>{
    // 로그인 처리       
    if(req.body.id && req.body.pw && req.body.id === req.body.pw){
        //로그인 성공으로 가정..
        //이후 이 유저 접속시에.. 로그인 상태 유지..
        req.session.loginId = req.body.id
        res.send(`
            <h3>${req.body.id}로그인 성공</h3>
            <a href="logout">로그아웃</a>
            <a href="/">홈으로</a>
        `)
    } else {
        res.send(`
            <h3>로그인 실패</h3>
            <a href='/'>홈으로</a>
        `)
    }
})

app.get('/logout', (req, res) => {
    // 로그인 상태 유지를 위해 id값을 유지하고 있음으로, 로그아웃 처리는 세션 삭제
    res.clearCookie('connect.sid') // 세션 설정시 name을 설정하지 않으면 기본 name이 connect.sid
    res.send(`
        <h3>로그아웃</h3>
        <a href='/'>홈으로</a>
    `)
})

app.listen(app.get('port'), ()=> {
    console.log(app.get('port'), '번 포트로 대기중')
})