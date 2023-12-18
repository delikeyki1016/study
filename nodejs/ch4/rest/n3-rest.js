// rest 
// 클라이언트 url 분석, method 분석
const http = require('http')
const fs = require('fs').promises
const path = require('path')

// database
const users = {}

// 서버 생성 
http.createServer(async (req, res)=>{
    try {
        //restful 서비스, 클라이언트요청의 method에 따라 처리해야 함
        //요청분석
        if (req.method === 'GET') {
            console.log('GET 요청url:', req.url)
            // 클라이언트 url분석
            if (req.url === '/'){
                // index.html 을 클라이언트에게 전송, __dirname : 서버가 실행되고 있는 현재의 디렉토리 
                const data = await fs.readFile(path.join(__dirname, 'rest/index.html'))
                res.writeHead(200, {'Content-Type': 'text/html; charset=utf-8'}) // response header에 담길 내용
                return res.end(data) // response body에 담길 내용 
            } else if (req.url === '/about') {
                const data = await fs.readFile(path.join(__dirname, 'rest/about.html'))
                res.writeHead(200, {'Content-Type': 'text/html; charset=utf-8'})
                return res.end(data)
            } else if (req.url === '/users') { // 자바스크립트에서 ajax로 요청들어온 경우는 data를 요청한 것 
                res.writeHead(200, {'Content-Type': 'application/json; charset=utf-8'})
                console.log('users 데이터', users)
                return res.end(JSON.stringify(users)) // stringify 문자열화하다
            }

            // 그외의 요청이 들어온다면(css,js등..)
            const data = await fs.readFile(path.join(__dirname, req.url))
            return res.end(data)

        } else if (req.method === 'POST') {
            console.log('POST 요청url:', req.url)
            if (req.url === '/user') {
                let body = ''
                // 스트림 방식으로 클라이언트 데이터를 받겠다.
                req.on('data', (data)=>{
                    body += data
                })
                // 모두 읽은 후
                return req.on('end', ()=>{
                    console.log('post...바디', body)
                    const {name} = JSON.parse(body) // 네트워킹 데이터는 문자열이다. 이 문자열을 json으로 변형
                    const id = Date.now() // 유저를 식별할 id값으로 사용하려고.
                    users[id] = name
                    res.writeHead(201, {'Content-Type': 'text/plain; charset=utf-8'}) // text/plain 평문 문자열
                    res.end('등록성공')
                })
            }
        } else if (req.method === 'PUT') {
            console.log('PUT 요청url:', req.url)
            if(req.url.startsWith('/user/')){
                // url에서 key 값 획득
                const key = req.url.split('/')[2] 
                let body = ''
                // 수정할 데이터를 받아서 
                req.on('data', (data) => {
                    body += data
                })
                return req.on('end', ()=> {
                    console.log('put...', body)
                    users[key] = JSON.parse(body).name
                    res.writeHead(201, {'Content-Type': 'text/plain; charset=utf-8'})
                    res.end(JSON.stringify(users))
                })
            }
        } else if (req.method === 'DELETE') {
            console.log('DELETE 요청url:', req.url)
            if(req.url.startsWith('/user/')) {
                const key = req.url.split('/')[2]
                delete users[key]
                res.writeHead(201, {'Content-Type': 'text/plain; charset=utf-8'})
                return res.end(JSON.stringify(users))
            }
        }
        const data = await fs.readFile('./response.html')
        res.writeHead(200, {'Content-Type':'text/html; charset=uft-8'})
        res.end(data)
    } catch(err){
        console.error(err)
        res.writeHead(500, {'Content-Type':'text/plain; charset=uft-8'})
        res.end(err.message)
    }
}).listen(8080, ()=> console.log('8080포트 구동'))