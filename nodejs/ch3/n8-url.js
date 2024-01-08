const url = require('url')

const { URL } = url

const myUrl = new URL('https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=%EC%9E%90%EB%B0%94%EC%8A%A4%ED%81%AC%EB%A6%BD%ED%8A%B8')

console.log('myUrl', myUrl)

// url객체를 문자열로 변환
console.log('포맷', url.format(myUrl))

// url애서 쿼리 문자열만 획득
console.log('쿼리', myUrl.searchParams)

// 쿼리문자열은 key=value 형태. 키를 명시해서 특정데이터 추출
console.log('모두 추출', myUrl.searchParams.getAll('where'))
console.log('하나만 추출', myUrl.searchParams.get('q'))

// 모든 키 값 획득
console.log('모든 키 값', myUrl.searchParams.keys())
// 모든 값 획득
console.log('모든 값', myUrl.searchParams.values())


// 동적으로 쿼리 문자열 만들기
myUrl.searchParams.append('aaa','bbb') //(키값, 밸류값)
console.log('포맷', url.format(myUrl))

//해당 키쿼리 문자열 변경 
myUrl.searchParams.set('aaa', 'ccc')
console.log('포맷', url.format(myUrl))