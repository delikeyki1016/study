// file system 
// file read, write(I/O) API는 자동으로 콜백함수를 백그라운드로 보낸다. 실행순서는 테스트할 때 마다 차이가 있을 수 있다. 

//callback 방식
const fs1 = require('fs')

// 파일을 생성한 후 쓰기
fs1.writeFile('./sample.txt', '안녕하세요, 반갑습니다.', (err)=>{
    if (err) {
        throw err
    }
    // 성공하면 파일 읽기
    fs1.readFile('./sample.txt', (err, data)=>{
        if (err) {
            throw err
        }
        console.log(data.toString())
    })
})

// promises 방식
const fs2 = require('fs').promises

fs2.writeFile('./sample2.txt', 'promises 방식의 파일쓰기 입니다.')
    .then(()=>{
        return fs2.readFile('./sample2.txt')
    })
    .then((data)=>{
        console.log(data.toString())
    })
    .catch((err)=>{
        console.error(err)
    })

