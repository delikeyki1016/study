const fs = require('fs')
const crypto = require('crypto')

// 1. 긴 신문기사를 복사해 넣는다.
const article = `11월 말 샘 올트먼 오픈AI 최고경영자(CEO)가 회사에서 쫓겨났다가 닷새 만에 복직했다. 이와 관련해 소문이 무성했지만, 그중 유력한 소식 하나는 오픈AI가 회사 정체성에 혼란이 올 만큼 고도로 발전된 인공지능(AI)을 개발하고 있다는 것이다. 바로 ‘Q*(큐스타) 알고리즘’으로 불리는 AI 개발 프로젝트다. 현재 베일에 싸인 채 개발되고 있는 Q* 알고리즘은 인류를 위협할 강력한 AI 기술이라는 점에서 오픈AI 안팎에서 찬반양론을 불러일으키고 있다.
11월 말 샘 올트먼 오픈AI 최고경영자(CEO)가 회사에서 쫓겨났다가 닷새 만에 복직했다. 이와 관련해 소문이 무성했지만, 그중 유력한 소식 하나는 오픈AI가 회사 정체성에 혼란이 올 만큼 고도로 발전된 인공지능(AI)을 개발하고 있다는 것이다. 바로 ‘Q*(큐스타) 알고리즘’으로 불리는 AI 개발 프로젝트다. 현재 베일에 싸인 채 개발되고 있는 Q* 알고리즘은 인류를 위협할 강력한 AI 기술이라는 점에서 오픈AI 안팎에서 찬반양론을 불러일으키고 있다.
11월 말 샘 올트먼 오픈AI 최고경영자(CEO)가 회사에서 쫓겨났다가 닷새 만에 복직했다. 이와 관련해 소문이 무성했지만, 그중 유력한 소식 하나는 오픈AI가 회사 정체성에 혼란이 올 만큼 고도로 발전된 인공지능(AI)을 개발하고 있다는 것이다. 바로 ‘Q*(큐스타) 알고리즘’으로 불리는 AI 개발 프로젝트다. 현재 베일에 싸인 채 개발되고 있는 Q* 알고리즘은 인류를 위협할 강력한 AI 기술이라는 점에서 오픈AI 안팎에서 찬반양론을 불러일으키고 있다.
11월 말 샘 올트먼 오픈AI 최고경영자(CEO)가 회사에서 쫓겨났다가 닷새 만에 복직했다. 이와 관련해 소문이 무성했지만, 그중 유력한 소식 하나는 오픈AI가 회사 정체성에 혼란이 올 만큼 고도로 발전된 인공지능(AI)을 개발하고 있다는 것이다. 바로 ‘Q*(큐스타) 알고리즘’으로 불리는 AI 개발 프로젝트다. 현재 베일에 싸인 채 개발되고 있는 Q* 알고리즘은 인류를 위협할 강력한 AI 기술이라는 점에서 오픈AI 안팎에서 찬반양론을 불러일으키고 있다.
11월 말 샘 올트먼 오픈AI 최고경영자(CEO)가 회사에서 쫓겨났다가 닷새 만에 복직했다. 이와 관련해 소문이 무성했지만, 그중 유력한 소식 하나는 오픈AI가 회사 정체성에 혼란이 올 만큼 고도로 발전된 인공지능(AI)을 개발하고 있다는 것이다. 바로 ‘Q*(큐스타) 알고리즘’으로 불리는 AI 개발 프로젝트다. 현재 베일에 싸인 채 개발되고 있는 Q* 알고리즘은 인류를 위협할 강력한 AI 기술이라는 점에서 오픈AI 안팎에서 찬반양론을 불러일으키고 있다.
11월 말 샘 올트먼 오픈AI 최고경영자(CEO)가 회사에서 쫓겨났다가 닷새 만에 복직했다. 이와 관련해 소문이 무성했지만, 그중 유력한 소식 하나는 오픈AI가 회사 정체성에 혼란이 올 만큼 고도로 발전된 인공지능(AI)을 개발하고 있다는 것이다. 바로 ‘Q*(큐스타) 알고리즘’으로 불리는 AI 개발 프로젝트다. 현재 베일에 싸인 채 개발되고 있는 Q* 알고리즘은 인류를 위협할 강력한 AI 기술이라는 점에서 오픈AI 안팎에서 찬반양론을 불러일으키고 있다.
11월 말 샘 올트먼 오픈AI 최고경영자(CEO)가 회사에서 쫓겨났다가 닷새 만에 복직했다. 이와 관련해 소문이 무성했지만, 그중 유력한 소식 하나는 오픈AI가 회사 정체성에 혼란이 올 만큼 고도로 발전된 인공지능(AI)을 개발하고 있다는 것이다. 바로 ‘Q*(큐스타) 알고리즘’으로 불리는 AI 개발 프로젝트다. 현재 베일에 싸인 채 개발되고 있는 Q* 알고리즘은 인류를 위협할 강력한 AI 기술이라는 점에서 오픈AI 안팎에서 찬반양론을 불러일으키고 있다.
11월 말 샘 올트먼 오픈AI 최고경영자(CEO)가 회사에서 쫓겨났다가 닷새 만에 복직했다. 이와 관련해 소문이 무성했지만, 그중 유력한 소식 하나는 오픈AI가 회사 정체성에 혼란이 올 만큼 고도로 발전된 인공지능(AI)을 개발하고 있다는 것이다. 바로 ‘Q*(큐스타) 알고리즘’으로 불리는 AI 개발 프로젝트다. 현재 베일에 싸인 채 개발되고 있는 Q* 알고리즘은 인류를 위협할 강력한 AI 기술이라는 점에서 오픈AI 안팎에서 찬반양론을 불러일으키고 있다.
11월 말 샘 올트먼 오픈AI 최고경영자(CEO)가 회사에서 쫓겨났다가 닷새 만에 복직했다. 이와 관련해 소문이 무성했지만, 그중 유력한 소식 하나는 오픈AI가 회사 정체성에 혼란이 올 만큼 고도로 발전된 인공지능(AI)을 개발하고 있다는 것이다. 바로 ‘Q*(큐스타) 알고리즘’으로 불리는 AI 개발 프로젝트다. 현재 베일에 싸인 채 개발되고 있는 Q* 알고리즘은 인류를 위협할 강력한 AI 기술이라는 점에서 오픈AI 안팎에서 찬반양론을 불러일으키고 있다.
11월 말 샘 올트먼 오픈AI 최고경영자(CEO)가 회사에서 쫓겨났다가 닷새 만에 복직했다. 이와 관련해 소문이 무성했지만, 그중 유력한 소식 하나는 오픈AI가 회사 정체성에 혼란이 올 만큼 고도로 발전된 인공지능(AI)을 개발하고 있다는 것이다. 바로 ‘Q*(큐스타) 알고리즘’으로 불리는 AI 개발 프로젝트다. 현재 베일에 싸인 채 개발되고 있는 Q* 알고리즘은 인류를 위협할 강력한 AI 기술이라는 점에서 오픈AI 안팎에서 찬반양론을 불러일으키고 있다.
11월 말 샘 올트먼 오픈AI 최고경영자(CEO)가 회사에서 쫓겨났다가 닷새 만에 복직했다. 이와 관련해 소문이 무성했지만, 그중 유력한 소식 하나는 오픈AI가 회사 정체성에 혼란이 올 만큼 고도로 발전된 인공지능(AI)을 개발하고 있다는 것이다. 바로 ‘Q*(큐스타) 알고리즘’으로 불리는 AI 개발 프로젝트다. 현재 베일에 싸인 채 개발되고 있는 Q* 알고리즘은 인류를 위협할 강력한 AI 기술이라는 점에서 오픈AI 안팎에서 찬반양론을 불러일으키고 있다.
`

// 2. 작업 폴더에 quiz.txt 파일을 만든다
// 파일생성
const writeStream = fs.createWriteStream('./quiz.txt', {highWaterMark: 8})
writeStream.write(article)
writeStream.end(()=> console.log('파일쓰기 끝'))
writeStream.on('finish', ()=> {
    console.log('파일생성 후 쓰기 끝')
    
    //파일읽기
    const readStream = fs.createReadStream('./quiz.txt', {highWaterMark: 8}) 
    const data = []
    readStream.on('data', (chunk)=> {
        data.push(chunk)
    }) 
    readStream.on('end', ()=> { 
        let readData = Buffer.concat(data).toString()
        console.log(readData)

        // 3. 읽기작업이 완료되면 aes-256-cbc 알고리즘으로 읽은 데이터를 암호화 한다. 
        const algorithm = 'aes-256-cbc'
        const key = process.env.MY_quiz_key
        const iv = process.env.MY_quiz_iv 

        const cipher = crypto.createCipheriv(algorithm, key, iv)
        let result = cipher.update(readData, 'utf8', 'base64')
        result += cipher.final('base64')

        // 4. quiz-chipher.txt 파일에 암호화된 문자열을 쓴다.
        const writeStream1 = fs.createWriteStream('./quiz-chipher.txt')
        writeStream1.write(result)
        writeStream1.end() 
    })
})

// write가 끝나지 않았을 때 read하려고 시도했을 것이다. 그것을 수정 

// console.log(readData) 위의 end 부분은 비동기 실행입니다. 
// 그럼으로 console.log(readData) 가 실행되는 시점은 데이터가 없는게 맞지 않을까요?



