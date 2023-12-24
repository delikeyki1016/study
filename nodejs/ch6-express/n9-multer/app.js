// multer : 파일업로드 모듈 npm i multer 

const express = require('express')
const morgan = require('morgan')
const path = require('path')
const multer = require('multer')
const fs = require('fs')

const app = express()
app.set('port', process.env.PORT || 3000)

app.use(morgan('dev'))
app.use(express.urlencoded({extended: true}))

// upload 설정
const upload = multer({
    // 저장 위치 설정. 클라우드 스토리지도 제공한다.
    storage: multer.diskStorage({
        destination(req, file, done) {
            done(null, 'uploads/') // 디렉토리 설정, 첫번째 매개변수가 null이 아니면 에러상황이다. 
        },
        filename(req, file, done){ // file name 결정
            const ext = path.extname(file.originalname)
            done(null, path.basename(file.originalname, ext) + '_' + Date.now() + ext)
        }
    }),
    limits: {fileSize: 5*1024*1024} //5메가
})

app.get('/', (req, res) => {
    res.sendFile(path.join(__dirname, 'index.html'))
})

// file1은 html form의 name
app.post('/upload', upload.array('file1'), (req, res) => { // upload.single 파일1개 업로드, upload.array 파일 여러개 업로드
    console.log(req.file)
    res.send('ok')
})

app.listen(app.get('port'), ()=> {
    console.log(app.get('port'), '번 포트로 대기중')
})