const fs = require('fs')

// fs 모듈의 기본은 비동기방식, 속도는 빠르지만 작업순서는 보장하지 않음 


// 작업을 순서대로(동기 방식) 진행해야되면 함수명+Sync 를 제공, 결과를 콜백으로 받는 것이 아니라, 함수의 리턴값으로 받음
console.log('시작..')
let data = fs.readFileSync('./sample.txt') // 함수가 끝날 때까지 대기(블록킹)함
console.log('스텝1', data.toString())

data = fs.readFileSync('./sample.txt') 
console.log('스텝2', data.toString())

data = fs.readFileSync('./sample.txt') 
console.log('스텝3', data.toString())

// 위의 경우 성능에 문제가 있을 수 있다. 
// 10명의 유저가 동시 접속했다면, 10번째 유저의 요청은 앞선 9명 유저의 요청이 모두 끝나야 처리된다.
// 아래는 유저의 요청을 모두 백그라운드로 이동함. 10명의 유저는 대기없이 요청을 모두 백그라운드로 보냄, 유저 한명 당의 1,2,3 실행 순서는 보장된다.
console.log('시작2...')
fs.readFile('./sample.txt', (err, data) => {
    if(err){
        throw err;
    }
    console.log('스텝1', data.toString())
    fs.readFile('./sample.txt', (err, data) => {
        if(err){
            throw err;
        }
        console.log('스텝2', data.toString())
        fs.readFile('./sample.txt', (err, data) => {
            if(err){
                throw err;
            }
            console.log('스텝3', data.toString())
        })
    })
})