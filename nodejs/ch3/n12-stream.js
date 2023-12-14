const fs = require('fs')

// write stream
// const writeStream = fs.createWriteStream('./sample3.txt')
// writeStream.on('finish', ()=> console.log('파일쓰기 끝')) // 쓰기 끝난 후에 처리할 로직이 있다면 등록
// writeStream.write('hellow world 1\n')
// writeStream.write('hellow world 2\n')
// writeStream.write('hellow world 3\n')
// writeStream.write('hellow world 4\n')
// writeStream.write('hellow world 5\n')
// writeStream.end() // 쓰기 끝

// read stream
const readStream = fs.createReadStream('./sample3.txt', {highWaterMark: 8}) // highWaterMark 버퍼사이즈 지정. 
const data = []
// 버퍼에서 데이터가 전달되어, 버퍼가 full 되었을 때, 버퍼에 쌓인 데이터를 보통 chunk라고 부름 
readStream.on('data', (chunk)=> {
    data.push(chunk)
    console.log('data', chunk, chunk.length)
}) 
readStream.on('end', ()=> { // 읽기 끝난 후 이벤트 등록
    console.log('읽기 끝')
    console.log(Buffer.concat(data).toString())
}) 
readStream.on('error', ()=> console.log(err))