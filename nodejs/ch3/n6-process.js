// 환경변수
console.log(process.env.PATH)
console.log(process.env.MY_MYSQL_KEY)

setImmediate(()=>{
    console.log('immediate') // 4
})

process.nextTick(()=>{
    console.log('nextTick') // 1
})

setTimeout(() => {
    console.log('timeout') //3
}, 0);

Promise.resolve().then(()=> console.log('promise')) // 2

// process.nextTick, promise : setTimeout, setInterval보다 우선순위가 높아서 백그라운드에서 먼저 실행됨 