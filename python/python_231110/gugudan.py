# 구구단 출력
# for i in range(2, 9+1) :
#     print(f'{i}단 ' + '=' * 7)
#     for j in range(1, 9+1) :
#         print(f'{i} x {j} = ', i*j)
#     print('\n')
    
# 입력받은 숫자의 해당하는 구구단 출력
dan_num = int(input())

for j in range(1, 9 + 1) :
#     print(f'{dan_num} * {j} = {dan_num * j}')
    print("%d * %d = %d" % (dan_num, j, dan_num * j))
    
# while 문 이용
j = 1
while j < 10 :
    print(f'{dan_num} * {j} = {dan_num * j}')
    j += 1
