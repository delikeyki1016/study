# 반씩 잘라서 찾기, sorted된 리스트의 경우  
def find_my_num(list, value):
    
    startIdx, endIdx = 0, len(list) - 1 # startIdx = 0, endIdx = 6
    탐색횟수 = 0
    while startIdx <= endIdx:
        탐색횟수 += 1
        midIdx = (startIdx + endIdx) // 2
        if value == list[midIdx]:
            print('탐색횟수:', 탐색횟수)
            return f'숫자의 인덱스: {midIdx}'
        elif value < list[midIdx]:
            endIdx = midIdx - 1
        elif value > list[midIdx]:
            startIdx = midIdx + 1
    print('탐색횟수:', 탐색횟수)
    return -1 
        
print(find_my_num([1, 2, 3, 4, 5, 6, 7], 5))
print(find_my_num([5, 4, 2, 7, 9, 6], 9))
