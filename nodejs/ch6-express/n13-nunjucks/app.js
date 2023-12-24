const express = require('express')
const nunjucks = require('nunjucks')

const app = express()
app.set('port', process.env.PORT || 3000)
app.set('view engine', 'html') // 뷰엔진으로는 nunjucks를 쓰겠다
nunjucks.configure('views', {
    express: app,
    watch: true //개발시에만 true 로 하자
})

app.get('/', (req, res) => {
    res.render('test', {
        name: 'kim',
        count: 10,
        isCheck: true,
        datas: [10,20,30],
        obj: {
            data1: 'hello',
            data2: 'world'
        }
    })
})

app.listen(app.get('port'), ()=> {
    console.log(app.get('port'), '번 포트로 대기중')
})

