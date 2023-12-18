const http = require('http')

http.createServer((req, res) => {
    console.log(req.url, req.headers.cookie)
    // 응답하면서 헤더에 쿠키데이터를 설정
    // header,body 전송 순서를 바꿀 수 없다
    res.writeHead(200, {'Set-Cookie':'mycookie=test'})
    res.end('hello cookie')
}).listen(8080, ()=>{
    console.log('8080 포트로 서버구동')
})