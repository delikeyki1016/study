// npm i express morgan mysql2 nunjucks sequelize sequelize-cli 
// npm i -D nodemon

// Sequelize가 Node.js의 ORM 라이브러리 (백엔드와 DB는 http연동이 안되기 때문에)
// ORM은 Object Relational Mapping의 줄임말로 객체와 데이타(관계)를 매핑
// sequelize-cli 에서 제공하는 명령어를 이용해서 프로그램 구조 설정 
// npx sequelize init

// models/index.js 에 초기 설정: 기존 내용 삭제 후 설정
// 워크벤치에서 nodejs 스키마 생성 

const express = require('express')
const path = require('path')
const morgan = require('morgan')
const nunjucks = require('nunjucks')

const { sequelize } = require('./models') // 파일명 명시하지 않으면 index.js 

const indexRouter = require('./routes')
const userRouter = require('./routes/users')
const commentRouter = require('./routes/comments')
const testRouter = require('./routes/test')

const app = express()
app.set('port', process.env.PORT || 3000)

app.set('view engine', 'html')
nunjucks.configure('views', { // views 폴더 셋팅
    express: app,
    watch: true 
})

// 데이터베이스 연결
sequelize.sync({force: false}) // 기존 테이블은 건드리지 않는다. / force:true => 기존 테이블이 존재하면 삭제하고 새로 만든다.
    .then(()=>{
        console.log('DB 연결 성공')
    })
    .catch((err)=>{
        console.error(err)
    })

app.use(morgan('dev'))
app.use(express.static(path.join(__dirname, 'public')))
app.use(express.json())
app.use(express.urlencoded({extended: true}))

// 요청 처리 
app.use('/', indexRouter)
app.use('/users', userRouter)
app.use('/comments', commentRouter)
app.use('/test', testRouter)

// 404 처리
app.use((req, res, next) => {
    const error = new Error(`${req.method} ${req.url} 라우터가 없습니다.`)
    error.status = 404
    next(error)
})
// 에러 처리 
app.use((err, req, res, next) => {
    res.locals.message = err.message
    res.locals.error = err
    res.status(err.status || 500)
    res.render('error') //views/error.html로 렌더해라 
})

app.listen(app.get('port'), ()=> {
    console.log(app.get('port'), '번 포트로 대기중')
})
