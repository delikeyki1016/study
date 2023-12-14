// 함수실행이 백그라운드로 이동하여 메인스레드가 논블로킹으로 실행된다.
const timeout = setTimeout(()=>{
    console.log('timeout log')
}, 1500)

const interval = setInterval(()=>{
    console.log('interval log')
}, 500)

const timeout2 = setTimeout(() => {
    console.log('timeout2 log')
}, 3000);

setTimeout(() => {
    clearTimeout(timeout2) // timeout 취소
    clearInterval(interval) // interval 취소
}, 2000);

// 즉시 실행인데, 백그라운드에서 실행됨
const immediate = setImmediate(()=>{
    console.log('immediate log')
})

const immediate2 = setImmediate(()=>{
    console.log('immediate2 log')
})

clearImmediate(immediate2)