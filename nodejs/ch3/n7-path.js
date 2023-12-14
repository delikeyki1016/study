const path = require('path')

// __filename : 현재노드가 실행되는 파일의 전체 경로
const currentPath = __filename
console.log('전체경로', currentPath)
console.log('디렉토리경로', path.dirname(currentPath))
console.log('확장자명', path.extname(currentPath))
console.log('파일명', path.basename(currentPath))
console.log('상세정보', path.parse(currentPath))