const express = require('express')
const indexRouter = require('./routes/index') //index는 생략가능 
const userRouter = require('./routes/user')
const productRouter = require('./routes/product')

const app = express()
app.set('port', process.env.PORT || 3000)

app.use(express.urlencoded({extended: true}))

// 각 파일로 분리된 라우팅 정보를 조합
app.use('/', indexRouter)
app.use('/user', userRouter)
app.use('/product', productRouter)


app.listen(app.get('port'), ()=> {
    console.log(app.get('port'), '번 포트로 대기중')
})