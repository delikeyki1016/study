## 문자열 - 내장함수
# count("찾을 문자열") : 개수를 세는 함수
# find("찾을 문자열") : 위치찾기
# find("찾을 문자열", 5) : 5번째부터 찾기 시작
# rfind("찾을 문자열) : 오른쪽부터 찾기 
# index() : find()와 동일 없으면 오류발생
# upper : 대문자로 바꿈 
# lower : 소문자로 변환 

## 사용자정의함수 예제
# 매개변수에 기본값 지정 가능 plus(v1 = 10, v2 = 20)
def plus(v1 = 10, v2 = 20):
    result = v1+v2
    return result

hap = 0
hap = plus(100,200)
print("plus의 합은 %d 입니다" %hap)

def calc(v1,v2,op):
    result = 0
    if op == '+':
        result = v1+v2
    elif op == '-':
        result = v1-v2
    elif op == '*':
        result = v1*v2
    elif op == '/':
        result = v1/v2
    else :
        print("연산자를 입력해주세요.+-*/")
    return result

res1 = calc(100,200,"*")
res2 = calc(100,200,"d")
print(res1, res2)

def func1() :
    global a 
    a = 10
    return print("func1()의 a값은 %d" % a)

def func2() :
    return print("func2()의 a값은 %d" % a)

a = 20

func2()
func1()


def multi(v1,v2) :
    resList = []
    res1 = v1 + v2
    res2 = v1 - v2
    res3 = v1 * v2
    res4 = v1 / v2 
    resList.append(res1)
    resList.append(res2)
    resList.append(res3)
    resList.append(res4)
    
    return resList

myList = multi(100,200)
print(myList)

## 매개변수 n개를 받을 때: *tuple 방법
def func6(*para) :
    result = 0
    print(type(para))
    for n in para :
        result += n
    return result

print(func6(10,20,30))
print(func6(10,20,30,40,50,60,70,80,90))

## 매개변수를 키:값으로 받을 때: **dictionary 방법
def func7(**para) :
    print(type(para))
    for v, m in para.items() : 
        print("%s ===> %d" % (v, m))
        
func7(트와이스=8, 블랙핑크=4, 소녀시대=5)

## 람다함수 : 익명함수 
# 변수명 = lambda 입력값 : 리턴값 
f2 = lambda x,y : x+y
print("람다함수", f2(2,3))


## map 사용 예제
# 기본
myList = [1,2,3,4,5]
add10 = lambda num : num + 10
print(add10(myList[0]))
# map사용
print(map(add10, myList)) #object형식이므로
print(list(map(add10, myList))) #list로 형변환시켜줌

# 두 배열의 합을 구하기
myList2 = [1,2,3,4,5]
myList3 = [10,20,30,40,50]
add2 = lambda n1, n2 : n1 + n2
print(list(map(add2, myList2, myList3)))

## 평균,평점 출력
def avg(*score) :
    score_sum, score_avg = 0, 0.0
    myScore = []
    for num in score :
        score_sum += num
        score_avg = score_sum / len(score)
        
    if score_avg >= 90 :
        grade = "A"
    elif score_avg >= 80 :
        grade = "B"
    elif score_avg >= 70 :
        grade = "C"
    elif score_avg >= 60 :
        grade = "D"
    else :
        grade = "F"
    
    myScore.append(score_avg)
    myScore.append(grade)

    return myScore

print(avg(80,70,90))

## 로또 추첨기
# if lotto.count(num) == 0 lotto리스트내에 num이 없냐(==0)? true 
# while true 조건이 참일때까지 돈다.
import random
def getNumber() :
    return random.randrange(1,46)

#1.랜덤숫자 뽑아옴 2.중복체크 중복되지않으면 []에담음 3.총개수가 6개면 종료 후 [] 반환
lotto = []
num = 0
while True :
    num = getNumber()
    if lotto.count(num) == 0 : #num이 0이라는 것은 num이 이 리스트에 없다는 뜻, 존재하면 1이다. 
        lotto.append(num)
    if len(lotto) >=6 :
        break 

lotto.sort()
print("로또번호는?",lotto)
    
