# idx= [0, 1, 2, 3, 4, 5]
list = [5, 4, 2, 6, 3, 1]

for i in range(len(list) - 1) :
    keyIdx = i # 0인덱스를 키인덱스로 설정
    for j in range(i+1, len(list)): # 1인덱스부터 끝까지 탐색
        if list[keyIdx] > list[j]: # 키인덱스값이 그다음인덱스값보다 크면, 키인덱스에 그다음인덱스를 넣어둠  
            keyIdx = j
    list[i], list[keyIdx] = list[keyIdx], list[i]

print(list)