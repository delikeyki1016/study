# 이름을 입력받아 동명이인인 것을 찾아 set에 담아 출력하기 
names = input().split()

names_dict = {}
names_set = set()

for i in names :
    if i in names_dict :
        names_dict[i] += 1
        names_set.add(i)
    else :
        names_dict[i] = 1

# for k, v in names_dict.items() :
#     if v >= 2 :
#         names_set.add(k)
        
print(names_dict)
print(names_set)



# 쌤 코드 
# names_dict = {i : names_dict.get(i,0) + 1 for i in names}
# 1. names를 반복해서 names_dict를 채워나간다.
# 1-1. names_dict에 이름이 있으면 +1, 없으면 1
# for i in names:
#     if i in names_dict:
#         names_dict[i] += 1
#     else:
#         names_dict[i] = 1

# names_set = set()
# # 2. names_dict를 반복해서 key, value를 가지고
# # 2-1. value가 2 이상이면 names_set에 추가
# for k, v in names_dict.items():
#     if v >= 2:
#         names_set.add(k)

# # 3. names_set 출력
# print(names_set)


# names_dict = {1:'aa', 2:'bb', 3:'cc'}
# for k,v in names_dict.items():
#     print(k,v)
# print(names_dict.items())



        