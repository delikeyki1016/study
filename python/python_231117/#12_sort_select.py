# 선택정렬 : 리스트에서 최소값을 골라 맨 앞으로 보내고, 
# 맨앞으로 보낸 요소를 제외한 나머지에서 다시 최소값을 골라 두번째자리로 보냄.이것을 반복
# chars = ['b','c','d','e','a']
chars = [7,5,9,0,3,1,6,2,4,8]

def selection_sorted(list):
    for i in range(len(list)-1):
        minIdx = i # 가장 작은 원소의 인덱스 
        for j in range(i + 1, len(list)):
            if list[minIdx] > list[j]:
                minIdx = j
        list[i], list[minIdx] = list[minIdx], list[i] # 스왑
    return list

print(selection_sorted(chars))

# chars.sort() # 원본이 변함
# sorted는 새롭게 반환 

# for i in chars: 
#     print(i) # i는 각 요소의 값 

# for i in range(len(chars)): 
#     print(i) # i는 index

# 하나씩 비교하면서 i가 크면 스왑 => 스왑이 더 많이 발생함 ㅠ 
# def selection_sorted(list):
#     for i in range(len(list)-1):
#         for j in range(i+1, len(list)):
#             if list[i] > list[j]:
#                 list[i], list[j] = list[j], list[i] 
#     return list
# print(selection_sorted(chars))