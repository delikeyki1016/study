// 1. reduce
// array : initialValue 설정을 안해줘도 숫자이기 때문에 더하는데 문제가 없다. 
// initialValue 설정을 하지않으면, accumulator=1(배열의 첫번째 값이 대입), currentNumber=2(배열의 두번째 값이 대입)로 시작함
// accumulator는 연산 후 결과값을 할당받음 
const numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
const sum = numbers.reduce((accumulator, currentNumber) => accumulator + currentNumber);
console.log(sum)

// object array
const friends = [
    {
        name: "양주진",
        age: 22,
    },
    {
        name: "오영제",
        age: 32,
    },
    {
        name: "서준형",
        age: 42,
    },
];

// initialValue 설정X => type error 발생 accumlattor는 {name: "양주진", age: 22} + currentObject.age는 오영제의 나이 32를 더하려고 시도하기 때문에 
const ageSum = friends.reduce((accumulator, currentObject) => {
    return accumulator + currentObject.age;
}, 0);

// 따라서 initialValue=0으로 설정하면, accumulator=0, currentObject.age=22이다.(양주진의 나이) 

console.log(ageSum)

const c1 = "name=홍길동;age=20;addr=서울"
// const parseCookies = (cookie = '') =>  
//     cookie
//         .split(';') // 여러건의 쿠키일 경우 구분자로 구분함. 잘린 문자열을 배열로 전달.
//         .map(v => v.split('=')) // 배열의 개수만큼 map() 내의 함수를 호출, =로 구분
//         .reduce((acc, [k,v]) => { //k 네임, v 밸류 
//             acc[k.trim()] = decodeURIComponent(v) //k.trim() 공백제거, decodeURIComponent 한글이 특수문자로 인코딩된 것을 다시 한글로 디코드
//             console.log(acc)
//             return acc //json data로 리턴
//         }, {}) // {}는 acc의 초기값 설정
// const result2 = parseCookies(c1)
// console.log(result2)

// split 함수 분리
const splitCookies = (cookie = '') => cookie.split(';')

// map 함수 분리
const mapCookies = (cookieArray) => cookieArray.map(v => v.split('='))

// reduce 함수 분리
const reduceCookies = (cookieArray) => {
    return cookieArray.reduce((acc, [k, v]) => {
        acc[k.trim()] = decodeURIComponent(v)
        console.log(acc)
        // { key1: 'value1' }
        // { key1: 'value1', key2: 'value2' }
        // { key1: 'value1', key2: 'value2', key3: 'value3' }
        return acc
    }, {})
};

// 최종 함수
const parseCookies = (cookie = '') => {
    const cookieArray = splitCookies(cookie)
    console.log(cookieArray) // [ 'key1=value1', ' key2=value2', ' key3=value3' ]
    const mappedCookies = mapCookies(cookieArray)
    console.log(mappedCookies) // [ [ 'key1', 'value1' ], [ ' key2', 'value2' ], [ ' key3', 'value3' ] ]
    const result = reduceCookies(mappedCookies)
    return result     
};

// 테스트
const cookieString = 'key1=value1; key2=value2; key3=value3'
const result = parseCookies(cookieString)
console.log(result)


// path __dirname
const path = require('path')
const url = path.join(__dirname, 'login.html')
console.log(url) // 현재 컴퓨터의 디렉토리 폴더/login.html 
