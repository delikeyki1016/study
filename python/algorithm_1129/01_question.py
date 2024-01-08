#이진탐색 
def find_my_num(list, value):
    start = 0
    end = len(list) - 1
    탐색횟수 = 0
    while start <= end :
        탐색횟수 += 1
        mid = (start + end) // 2
        if value == list[mid] : 
            print(탐색횟수)
            return mid
        elif value < list[mid]:
            end = mid - 1
        elif value > list[mid]:
            start = mid + 1
    print(탐색횟수)
    return -1

print(find_my_num([1,2,3,4,5,6,7,8], 6)) #2번만에 찾은 값5
print(find_my_num([1,2,3,4,5,6,7,8], 9)) #4번만에 찾은 값-1