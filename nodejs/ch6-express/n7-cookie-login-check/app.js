// cookie-parser (npm i cookie-parser)
const express = require('express')
const path = require('path')
const cookieParser = require('cookie-parser')

const app = express()
app.set('port', process.env.PORT || 3000)

app.use(cookieParser())
app.use(express.urlencoded({extended: true})) // 바디파서, client form 데이터 획득

app.get('/login', (req, res) => {
    res.sendFile(path.join(__dirname, 'loginForm.html'))
})

app.post('/login', (req, res) => {
    if(req.body.id_check && req.body.id_check == 'on') {
        // 유저가 전달한 id를 쿠키로 설정, 쿠키네임, 쿠키값, 옵션설정
        res.cookie('loginId', req.body.id, {
            maxAge: 60*1000
        })
    } else {
        // 체크가 안된상태, 쿠키설정되어있다면, 쿠키를 삭제시켜 id 출력 안되게 
        res.clearCookie('loginId', {})
    }
    res.sendFile(path.join(__dirname, 'loginOk.html'))
})

app.listen(app.get('port'), ()=> {
    console.log(app.get('port'), '번 포트로 대기중')
})