// node 제공 모듈은 경로 명시할 필요가 없다.
const express = require('express')
const path = require('path')

// 서버 준비
const app = express()
// app.set(), app 객체에 개발자 임의 데이터를 담을 수 있다. 그때 함수가 set()
app.set('port', process.env.PORT || 3000) //port를 셋팅함 process.env.PORT 또는 3000
console.log(process.env.PORT)

// get 방식 요청처리
app.get('/', (req, res)=>{
    // res.send('Hello world3 express')
    //express 를 사용하면 fs 모듈을 직접 사용하지 않아도 내부적으로 이용함
    res.sendFile(path.join(__dirname, '/index.html'))
})

// app에 담긴 데이터 획득
app.listen(app.get('port'), () => { // app.get('port') 을 3000으로 써도 됨
    console.log('3000 서버 실행 중..')
})


// express 환경 권장사항
// public : 그냥 다운로드만 하면 되는 static 파일들
// views : 서버사이드에서 동적처리한 후 응답하는 화면 관련 파일들
// routs : 요청 분석
// app.js : entry point js