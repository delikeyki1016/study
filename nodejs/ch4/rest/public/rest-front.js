// html 로딩시에 실행되어 서버에 user 데이터 요청 함수
async function getUser(){
    try {
        // 서버 요청 후 결과 res에 반환
        const res = await axios.get('/users')
        // res 화면에 출력
        const users = res.data
        console.log(users)
        const list = document.getElementById('list')
        list.innerHTML = ''
        // 여러건이 넘어오면, 반복 실행
        console.log(Object.keys(users)) // users json의 키를 배열로 만듬 
        // Object.keys() 로 배열을 만든다음에 그 배열의 갯수 만큼 map() 의 매개변수에 지정된 함수를 반복 호출
        Object.keys(users).map(function(key){
            const userDiv = document.createElement('div')
            const span = document.createElement('span')
            span.textContent = users[key]

            const edit = document.createElement('button')
            edit.textContent='수정'
            edit.addEventListener('click', async () => {
                const name = prompt('바꿀 이름을 입력하세요')
                if (!name) {
                    return alert('이름을 입력해주세요.')
                } 
                // method put 방식
                console.log('/user/' + key, {name})
                await axios.put('/user/' + key, {name})
                getUser()
            })

            const remove = document.createElement('button')
            remove.textContent='삭제'
            remove.addEventListener('click', async () => {
                // method delete 방식
                await axios.delete('/user/' + key)
                getUser()
            })

            // 동적으로 생성된 html태그를 화면에 출력 
            userDiv.appendChild(span)
            userDiv.appendChild(edit)
            userDiv.appendChild(remove)
            list.appendChild(userDiv)

        })
    } catch(err) {
        console.error(err)
    }
}

window.onload = getUser

// 등록 버튼을 눌렀을 때 이벤트 등록 
document.getElementById('form').addEventListener('submit', async (e) => {
    e.preventDefault(); // 버튼클릭 후 화면전환되지 않기 위해서 
    // 유저 입력 데이터 뽑기
    const name = e.target.userName.value
    if (!name) {
        return alert('이름을 입력하세요')
    }
    try {
        // 서버에 등록 요청
        await axios.post('./user', {name: name}) // {name} 키와 밸류가 같다면 이렇게도 쓸 수 있음 
        getUser()
    } catch(err) {
        console.error(err)
    }
    // input에 남아있는 문자 지우기
    e.target.userName.value = ''
})