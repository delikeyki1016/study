// network data는 header(설정된 정보내용)와 body(실제 넘기는 데이터)로 구성 
const http = require('http')

// 서버 생성 
const server = http.createServer((req, res) => {
    // response header 설정
    res.writeHead(200, {'Content-Type': 'text/html; charset=utf-8'})
    // response body 설정
    res.write(`<h1>hello node!</h1><p>You connect http server</p>`)
    res.end(`<h2>response end</h2>`)
})
// 요청 대기 
server.listen(8080)
server.on('listening', ()=>{
    console.log('서버가 구동되어 8080포트로 요청을 대기 중입니다.')
})
server.on('error', (err) => {
    console.error(err)
})


// const server1 = http.createServer((req, res) => {
//     res.writeHead(200, {'Content-Type': 'text/html; charset=utf-8'})
//     res.write(`<h1>server1 8081port</h1><p>You connect http server</p>`)
//     res.end()
// })
// server1.listen(8081)
// server1.on('listening', ()=>{
//     console.log('서버1이 구동되어 8081포트로 요청을 대기 중입니다.')
// })