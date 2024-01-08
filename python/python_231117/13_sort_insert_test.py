list = [5,4,2,6,3,1]

for i in range(1, len(list)):
    for j in range(i, 0, -1):
        if list[j-1] > list[j]:
            list[j], list[j-1] = list[j-1], list[j] #스왑 횟수가 11번
#         # else:
#         #     break

# 1인덱스의 값과 0인덱스의 값을 비교해서, 0인덱스 값이 크면 1인덱스에 0인덱스값을 넣는다. 
# for i in range(1, len(list)): 
#     key_value = list[i]
#     j = i - 1
#     while j >= 0 and list[j] > key_value:
#         list[j + 1] = list[j]
#         j -= 1
#     list[j+1] = key_value


print(list)