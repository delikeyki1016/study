# 올라가는 거리, 내려오는 거리, 전체 막대 길이

#2 1 5 = 4
#5 1 6 = 2
#100 99 1000000000 = 999999901

import sys 
a, b, v = [int(i) for i in sys.stdin.readline().split()]

# 3번째 케이스는 엄청 오래걸림 
day = 0
v_1 = a - b
while v_1 * day < v:
    day += 1
print(day)

# def snail_slow():
#     a, b, v = [int(i) for i in sys.stdin.readline().split()]
#     now = 0
#     day = 0
#     while now < v:
#         day += 1
#         now += a # 낮이 되었습니다. 
#         if now >= v:
#             break
#         now -= b # 밤이 되었습니다.
#     print(day)
    
# def snail_fast():
#     a, b, v = [int(i) for i in sys.stdin.readline().split()]
#     every_day = a- b
#     real_v = v - b # 낮에 끝나는 게 목표니까.
#     day = real_v // every_day
#     if real_v // every_day != 0:
#         day += 1
#     print(day)

# snail_fast()
