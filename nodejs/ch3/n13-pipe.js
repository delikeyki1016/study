const fs = require('fs')
const zlib = require('zlib') // 파일 압축관련 지원, gz로 압축함. zip으로 압축하려면 별도의 외부 모듈을 import 해야함

//파일 복사의 개념
const readStream = fs.createReadStream('./sample2.txt')
const writeStream = fs.createWriteStream('./sample2_write.txt')
readStream.pipe(writeStream)


const zlibStream = zlib.createGzip()
const writeStream2 = fs.createWriteStream('./sample2.txt.gz')
readStream.pipe(zlibStream).pipe(writeStream2)
