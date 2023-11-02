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
    

## 모듈Module : 함수의 집합, 모듈의 집합은 패키지 (함수 < 모듈 < 패키지) 패키지는 __init__.py 가 존재(보통 파일명이 대문자로 시작)
# import로 불러줌 import random => random 모듈을 호출함(모듈내의 모든 함수를 호출). random.randrange random 모듈 내에 randrange함수를 호출

# 모듈 import 방법 4가지 
# 1. import random
# 2. import random as rd => rd라는 별칭으로 사용할 것이다. 
# 3. from random import randrange => random모듈의 randrange만 호출해오겠다. 모듈이름을 앞에 붙이지 않고 사용할 수 있다. 메모리 절감
# 4. from random import * => random모듈의 모든함수 호출, 모듈이름 앞에 붙이지 않고 사용할 수 있다.


## 모듈 만들기 예제 Module1.py, import_Module1.py

## 모듈활용 : time, datetime 모듈
from time import *
print(localtime())

from datetime import *
print(date(2023, 12, 25) - date(2023, 10, 31))


#요일찍어보기
whatDay = localtime().tm_wday

def whatDayFunc(day) :
    days = ['월','화','수','목','금','토','일']
    return days[day]
    
print(whatDayFunc(whatDay))

## 파일 입출력
f = open("D:/multi/git_test/test3/law.txt", "r") #1.파일 오픈
contents = f.read() #2.파일 조작
f.close() #3.파일 닫기

print(contents)

#with as문으로 읽고,닫기
with open("D:/multi/git_test/test3/law.txt", "r") as f :
    contents = f.read()
    word_list = contents.split(" ") #list로 반환
    line_list = contents.split("\n") #list로 반환
    
print(contents)
print("문자수:", len(contents))
print("단어수:", len(word_list))
print("라인수:", len(line_list))

#한줄씩 읽어오기 readlines()
with open("D:/multi/git_test/test3/law.txt", "r") as f :
    contentList = f.readlines()

print(contentList, len(contentList)) #list로 반환
print(contentList[:5]) #처음부터 5개까지 프린트

#파일쓰기, with as로도 사용가능 
newFile = open("D:/multi/git_test/test3/new_text.txt", "w", encoding="utf-8") #w : write
for i in range(1,11) :
    data = "%d번째 줄 입니다.\n" % i
    newFile.write(data)
newFile.close()
    
newFile = open("D:/multi/git_test/test3/new_text.txt", "a", encoding="utf-8") #a : append
for i in range(11,21) :
    data = "%d번째 줄 입니다.\n" % i
    newFile.write(data)
newFile.close()

#CSV 파일 출력, csv : comma saperate value 
import csv

with open("D:/multi/git_test/test3/fruit.csv", "w", newline="") as csv_file :
    writer = csv.writer(csv_file, delimiter=',')
    writer.writerow(["apple", 5000])
    writer.writerow(["banana", 3000])
    writer.writerow(["cherry", 8500])

  
csv_file_open = open("D:/multi/git_test/test3/fruit.csv", "r")
csvRead = csv.reader(csv_file_open)
print(csvRead) #객체번호로 출력

fruit = []
for i in csvRead :
    fruit.append(i)
    print(i)

print(fruit)

# 예외처리 try except 문 => try : 실행문 except 예외종류 1 : 오류일때 실행문 except 예외종류 2 : 오류일 때 실행문 
# try(에러가 나올법한 실행문), except(에러가 나면 출력), else(에러가 안나면 출력), finally(에러가 있던지 없던지 출력)
import os

try :
    os.remove("D:/multi/git_test/test3/noFile.exe")
except :
    print("없는 파일입니다. 확인요망!")
 
 
    
num1 = input('숫자1:')
num2 = input('숫자2:')

try :
    num1 = int(num1) #숫자입력을 안한 경우 int로 변경 시 에러 발생함 
    num2 = int(num2)
    while True :
        res = num1 / num2 #num2가 0일 경우 에러 발생함 
        print(res)     #숫자를 정상으로 넣을 경우 계속 실행함.   
except ValueError :
    print("문자는 숫자로 변환할 수 없어요.")
except ZeroDivisionError :
    print("0으로는 나눌 수 없습니다.")
except KeyboardInterrupt :
    print("Ctrl+c를 눌렀군요") #ctrl+c를 누르면 계속실행을 스탑시킴 
    
    
# Class : 현실세계의 사물을 컴퓨터 안에서 구현하려고 고안된 개념
# 클래스 = 속성(정적특징, 변수라고 부르지않고 "필드field"라 부름) + 메서드(동적특징, 함수라 부르지않고 "method메서드"라 부름)
# 붕어빵틀 => 클래스(부모), 붕어빵s => 인스턴스(자식) ex) 붕어빵1 = 붕어빵틀() => 인스턴스명 = 클래스명()
# self.속성명(필드) => self가 this
class Car : # 1.클래스선언
    color = ""
    speed = 0
    def upSpeed(self, value) :
        speed += value
        
myCar1 = Car()  # 2. 인스턴스 생성
myCar1.color = "빨강" # 3. 필드나 메서드 사용
myCar1.upSpeed(30)
