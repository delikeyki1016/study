const http = require('http')
const fs = require('fs').promises
const path = require('path')


const parseCookies = (cookie = '') =>  
    cookie
    .split(';') 
    .map(v => v.split('='))
    .reduce((acc, [k,v]) => { 
        acc[k.trim()] = decodeURIComponent(v) 
        return acc 
    }, {}) 

// 클라이언트 상태 정보를 저장하기 위한 변수 
const session = {}

http.createServer(async (req, res)=>{
    const cookies = parseCookies(req.headers.cookie)

    if (req.url.startsWith('/login')) {
        const url = new URL(req.url, 'http://localhost:8080')
        const name = url.searchParams.get('name')

        const expire = new Date()
        expire.setMinutes(expire.getMinutes() + 5)  

        // 상태 데이터를 식별하기 위한 식별자(session id) 준비
        const uniqueInt = Date.now()
        session[uniqueInt] = {name, expire}

        // 상태 데이터는 서버사이드에 세션 id는 쿠키기술로 클라이언트 사이드로 넘김 
        res.writeHead(302, {
            Location: '/',
            'Set-Cookie': `session=${uniqueInt};Expires=${expire.toGMTString()};HttpOnly;Path=/`
        }) 
        res.end() 
    } else if (cookies.session && session[cookies.session].expire > new Date()) {
        res.writeHead(200, {'Content-Type':'text/plain; charset=utf-8'})
        res.end(`${session[cookies.session].name} 님 안녕하세요.`)
    } else {
        const data = await fs.readFile(path.join(__dirname, 'login.html'))
        res.writeHead(200, {'Content-Type':'text/html; charset=utf-8'})
        res.end(data)
    }
}).listen(8080, () => console.log("8080 포트로 서버 구동 후 대기함"))