## 모듈Module : 함수의 집합, 모듈의 집합은 패키지 (함수 < 모듈 < 패키지) 패키지는 __init__.py 가 존재(보통 파일명이 대문자로 시작)
# import로 불러줌 import random => random 모듈을 호출함(모듈내의 모든 함수를 호출). random.randrange random 모듈 내에 randrange함수를 호출

# 모듈 import 방법 4가지 
# 1. import random
# 2. import random as rd => rd라는 별칭으로 사용할 것이다. 
# 3. from random import randrange => random모듈의 randrange만 호출해오겠다. 모듈이름을 앞에 붙이지 않고 사용할 수 있다. 메모리 절감
# 4. from random import * => random모듈의 모든함수 호출, 모듈이름 앞에 붙이지 않고 사용할 수 있다.


## 모듈 만들기 예제 Module1.py, import_Module1.py (파일명 대문자로 시작)

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
    
print('요일찍어보기',localtime())
print('요일찍어보기',whatDayFunc(whatDay))

## 파일 입출력
f = open("D:/multi/study/python/law.txt", "r") #1.파일 오픈
contents = f.read() #2.파일 조작
f.close() #3.파일 닫기

print(contents)

#with as문으로 읽고,닫기
with open("D:/multi/study/python/law.txt", "r") as f :
    contents = f.read()
    word_list = contents.split(" ") #list로 반환
    line_list = contents.split("\n") #list로 반환
    
print(contents)
print("문자수:", len(contents))
print("단어수:", len(word_list))
print("라인수:", len(line_list))

#한줄씩 읽어오기 readlines()
with open("D:/multi/study/python/law.txt", "r") as f :
    contentList = f.readlines()

print(contentList, len(contentList)) #list로 반환
print(contentList[:5]) #처음부터 5개까지 프린트

#파일쓰기, with as로도 사용가능 
newFile = open("D:/multi/study/python/new_text.txt", "w", encoding="utf-8") #w : write
for i in range(1,11) :
    data = "%d번째 줄 입니다.\n" % i
    newFile.write(data)
newFile.close()
    
newFile = open("D:/multi/study/python/new_text.txt", "a", encoding="utf-8") #a : append
for i in range(11,21) :
    data = "%d번째 줄 입니다.\n" % i
    newFile.write(data)
newFile.close()

#CSV 파일 출력, csv : comma separated value 
import csv

with open("D:/multi/study/python/fruit.csv", "w", newline="") as csv_file :
    writer = csv.writer(csv_file, delimiter=',')
    writer.writerow(["apple", 5000])
    writer.writerow(["banana", 3000])
    writer.writerow(["cherry", 8500])

  
csv_file_open = open("D:/multi/study/python/fruit.csv", "r")
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
    os.remove("D:/multi/study/python/noFile.exe")
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