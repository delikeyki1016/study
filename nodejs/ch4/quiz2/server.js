const http = require('http')
const fs = require('fs').promises
const path = require('path')

// 응답받을 데이터 변수
const users = {}

http.createServer(async (req, res)=>{
    try {
        if (req.method === 'GET') {
            if (req.url === '/'){
                const data = await fs.readFile(path.join(__dirname, 'login.html'))
                res.writeHead(200, {'Content-Type': 'text/html; charset=utf-8'}) 
                return res.end(data)
            } 
            // 그외의 요청이 들어온다면(css,js등..)
            const data = await fs.readFile(path.join(__dirname, req.url))
            return res.end(data)

        } else if (req.method === 'POST') {
            if (req.url === '/login'){
                let body = ''
                req.on('data', (data)=>{
                    body += data
                })
                return req.on('end', ()=>{
                    console.log('post...바디', body)
                    const {id, password} = JSON.parse(body)
                    users['id'] = id
                    users['password'] = password
                    console.log(users)
                    res.writeHead(201, {'Content-Type': 'text/plain; charset=utf-8'})
                    res.end(JSON.stringify(users))
                })
            }
        } 

    } catch(err){
        console.error(err)
        res.writeHead(500, {'Content-Type':'text/plain; charset=uft-8'})
        res.end(err.message)
    }
}).listen(8080, ()=> console.log('8080포트 구동'))