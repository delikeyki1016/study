const http = require('http')
const fs = require('fs').promises
const path = require('path')

// 매개변수로 전달되는 쿠키를 분석해서 json object로 만들어 주는 개발자 함수 
const parseCookies = (cookie = '') =>  // 쿠키가 전달이 안되면, cookie = '' 디폴트값 설정함 
    cookie
        .split(';') // 여러건의 쿠키일 경우 구분자로 구분함. 잘린 문자열을 배열로 전달.
        .map(v => v.split('=')) // 배열의 개수만큼 map() 내의 함수를 호출, =로 구분
        .reduce((acc, [k,v]) => { //k 네임, v 밸류 
            acc[k.trim()] = decodeURIComponent(v) //k.trim() 공백제거, decodeURIComponent 한글이 특수문자로 인코딩된 것을 다시 한글로 디코드
            return acc //json data로 리턴
        }, {}) //?


http.createServer(async (req, res)=>{
    // 요청에서 cookie 추출
    console.log(req.headers.cookie)
    const cookies = parseCookies(req.headers.cookie)

    if (req.url.startsWith('/login')) {
        // 유저가 입력한 name 데이터 추출
        const url = new URL(req.url, 'http://localhost:8080')
        console.log('url:', url)
        //http://localhost:8080/login?name=kim
        const name = url.searchParams.get('name')

        // cookie 설정 : 유저가 입력한 name을 그대로 cookie에 담자
        const expire = new Date()
        expire.setMinutes(expire.getMinutes() + 5) // 현재시간 + 5분으로 설정 
        res.writeHead(302, {
            Location: '/',
            'Set-Cookie': `name=${encodeURIComponent(name)};Expires=${expire.toGMTString()};HttpOnly;Path=/`
        }) //302 브라우저에게 지정한 url로 redirect (300번대는 redirect)
        res.end() // 응답body는 없고, 응답헤더에 redirect 명령이 들어갔기 때문에, body 데이터는 의미가 없다.
    } else if (cookies.name) {
        // 쿠키를 분석했더니, name 데이터가 있다면
        res.writeHead(200, {'Content-Type':'text/plain; charset=utf-8'})
        res.end(`${cookies.name} 님 안녕하세요.`)
    } else {
        // url이 /login도 아니고, 쿠키도 없다면 
        const data = await fs.readFile(path.join(__dirname, 'login.html'))
        res.writeHead(200, {'Content-Type':'text/html; charset=utf-8'})
        res.end(data)
    }
}).listen(8080, () => console.log("8080 포트로 서버 구동 후 대기함"))