let data = 10
function myFun3(){}
class MyClass3 {
    data2 = 20
}

// 하나씩 export 하는 경우 
// exports.xxx(외부 노출 이름) = yyy(파일 내의 이름)
// exports.myData = data

// json 형식으로 exports, key, value가 같으면 한개만 써도 되니까. 
module.exports = {
    data,
    myFun22: myFun3,
    MyClass3
}