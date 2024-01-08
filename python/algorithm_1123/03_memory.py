str = 'apple'
print(id('apple'), id('banana'), id(str)) # id는 메모리 주소를 가르킴 

str = 'banana'
print(id('apple'), id('banana'), id(str)) # str은 참조주소를 바나나의 주소로 바꿨다. # 즉 문자열은 불변객체이다. 

# set와 dict key의 값에는 가변객체가 들어올 수 없다. 
# my_set = set([[1,2,3], 4])  에러
# my_dict = {}


# copy
import copy
list_a = [1,2,3]
list_b = list_a # list_c = list_a[:] 과 같음 

print(list_a == list_b)  # 값을 비교 
print(list_a is list_b)  # 메모리 주소를 비교 

list_a.append(4)
print(list_a)
print(list_b)

list_c = copy.deepcopy(list_a) # 깊은 복사
# list_c = list_a[:] 은 얇은 복사
print(list_a == list_c)
print(list_a is list_c)
list_a.append(5)
print(list_a)
print(list_c)
print(list_a == list_c)
print(list_a is list_c)


