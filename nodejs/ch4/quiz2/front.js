document.getElementById('form').addEventListener('submit', async (e) => {
    e.preventDefault() // 버튼클릭 후 화면전환되지 않기 위해서 
    // 유저 입력 데이터 뽑기
    const id = e.target.id.value
    const password = e.target.password.value
    if (!id) {
        return alert('이름을 입력하세요')
    } else if (!password) {
        return alert('패스워드를 입력하세요')
    }
    // 서버에 등록 요청
    const resultData = await axios.post('/login', {id, password})
    alert(JSON.stringify(resultData.data))
    // input에 남아있는 문자 지우기
    e.target.id.value = ''
    e.target.password.value = ''
})