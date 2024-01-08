num = 3

# def hanoi(value):
#     if value == 1:
#         return 1
#     # return 1 + (2 * hanoi(value-1))
#     first = hanoi(value-1)
#     second = 1
#     third = hanoi(value-1)
#     return first+second+third
    
# print(hanoi(num))

# value 원반수, start 시작기둥, end 목적지 기둥, mid 경유지 기둥
def hanoi_detail(value, start, end, mid):
    if value == 1:
        print(f'{value}번 원반을 {start} -> {end} 이동')
        return
    hanoi_detail(value-1, start, mid, end)
    print(f'{value}번 원반을 {start} -> {end} 이동')
    hanoi_detail(value-1, mid, end, start)
    return

print(2 ** num - 1) 
hanoi_detail(num, 1,3,2)
