const fs = require('fs')

// access 함수:  원하는 파일이 있는지 여부 확인, 있다면 read,write 가능여부 판단
// fs.access('./subdir', fs.constants.F_OK | fs.constants.R_OK | fs.constants.W_OK, (err) => {
//     if (err) {
//         if(err.code === 'ENOENT'){ //파일이나 폴더가 없는 경우
//             console.log('해당 파일이나 폴더 없음')
//             //폴더 생성
//             fs.mkdir('./subdir', (err) => {
//                 console.log('폴더생성 성공')
//                 // 파일생성
//                 fs.open('./subdir/file.js', 'w', (err) => { //file.js 파일 생성 'w' : write
//                     console.log('파일 생성 성공')
//                     // 파일명 변경
//                     fs.rename('./subdir/file.js', './subdir/newfile.js', (err) => {
//                         console.log('파일명 변경 성공')
//                     })
//                 })
//             })
//         }
//     } else {
//         console.log('이미 존재하는 폴더입니다.')
//     }
// })

// 디렉토리 내용 보기
fs.readdir('./subdir', (err, dir) => {
    if (err) {
        console.log(err)
    } else {
        console.log('폴더 내용', dir)
    }    
    // 파일 삭제 
    fs.unlink('./subdir/newfile.js', (err) => {
        if (err) {
            console.log(err)
        } else {
            console.log('파일삭제 성공')
        }
        
        // 폴더 삭제 
        fs.rmdir('./subdir', (err)=>{
            if (err) {
                console.log(err)
            } else {
                console.log('폴더삭제 성공')
            }  
        })
    })
})