# 구조분해할당
hong_list = ['hong', 20]
name, age = hong_list
print(name) #hong
print(age) #20

eight_divisor = [1,2,4,8]
odd, *even = eight_divisor
print(odd, even) # 1, [2,4,8]

kim_list = ['kimsu', 'TMI', 30, 'TMI', 'kangnam']
name, _, age, _, address = kim_list
print(name, age, address)

park_list = ['park', 'TMI1', 'TMI2', 'TMI3', 'mables']
name, *_, works = park_list #*은 항상 리스트를 반환
print(name,works)
print(_)

# 기존리스트를 이용해 신규 리스트 생성 
num_list = [1,2,3,4]
even_list = []
for element in num_list :
    even_list.append(element * 2)
print(even_list)

# list comprehension 적용
even_list = [element*2 for element in num_list if element%2 == 1]
print(even_list)

names = ['강민서', '강은영', '권보경', '박종섭', '박준영', '서유경', '신혜인', '유재현', '이지은', '천다영', '최아별', '최지성']

gangs = [i for i in names if i[0] == '강']
print(gangs)
choi_gangs = [i for i in names if i[0] == '강' or i[0] == '최']
print(choi_gangs)


