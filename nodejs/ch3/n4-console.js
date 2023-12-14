const string = 'abc'
const number = 1
const boolean = true
const obj = {
    outer: {
        inside: {
            key: 'value'
        }
    }
}

// 2
console.time('전체시간')

console.log(string, number, boolean)
// 객체의 depth를 볼 수 있다. 
console.dir(obj, {colors: false, depth: 2})
console.dir(obj, {colors: true, depth: 1})
// 로그를 테이블 형식으로 출력
console.table([{name: 'kim', age: 30}, {name:'lee', age: 25}])

// 1
console.time('시간측정')
for (let i = 0; i < 100000; i++){}
for (let i = 0; i < 100000; i++){}
console.timeEnd('시간측정')
// ~1

function b(){
    console.trace('b함수 호출 위치추적')
}
function a(){
    b()
}
a()

console.timeEnd('전체시간')
// ~2