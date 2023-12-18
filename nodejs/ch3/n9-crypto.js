// 단방향(해시), 양방향 모두 제공
const crypto = require('crypto')

// 해시는 복호화가 안되는 방식 : 비밀번호 
console.log('base64', crypto.createHash('sha512').update('1234').digest('base64')) //인코딩 base64
console.log('hex', crypto.createHash('sha512').update('1234').digest('hex')) //인코딩 hex
console.log('base64', crypto.createHash('sha512').update('1234').digest('base64'))


// 암호화 방법
const algorithm = 'aes-256-cbc'
// 알고리즘에 따라 키의 길이를 다르게. ex) 256/8 = 32, 192/8 = 24
const key = '12345678901234567890123456789012'
// iv : initialize vector
const iv = '1234567890123456' // 16자리

// 비대칭키를 만들려면 암호화하는 키(public key)와 복호화하는 키(private key)를 다르게 만들면 된다. 보안에 더 효과적 
// 아래는 대칭키로 진행된 것
// 암호화 
const cipher = crypto.createCipheriv(algorithm, key, iv)
let result = cipher.update('안녕하세요', 'utf8', 'base64')
result += cipher.final('base64') // 완료 별도 명시
console.log('암호화된 데이터', result)

// 복호화 
const decipher = crypto.createDecipheriv(algorithm, key, iv)
let result2 = decipher.update(result, 'base64', 'utf8') // 인코딩을 암호화와 반대로
result2 += decipher.final('utf8')
console.log('복호화된 데이터', result2)