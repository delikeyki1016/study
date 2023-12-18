const http = require('http')
const fs = require('fs').promises

http.createServer(async (req, res)=>{
    try {
        // await 뒷 부분이 실행완료될 때까지 대기하고, 완료되면 data에 대입(await는 async와 함께 사용)
        const data = await fs.readFile('./public/response.html')
        res.writeHead(200, {'Content-Type':'text/html; charset=uft-8'})
        res.end(data)
    } catch(err){
        console.error(err)
        // Content-Type: text/plain 일반 문자열, image/jpeg 이미지jpeg, text/html html파일
        res.writeHead(500, {'Content-Type':'text/plain; charset=uft-8'})
        res.end(err.message)
    }
})
.listen(8080, ()=> console.log('8080포트 구동'))
