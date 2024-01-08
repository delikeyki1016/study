# https://www.acmicpc.net/problem/10773
import sys
N = int(sys.stdin.readline())
stack = []
for _ in range(N):
    num = int(sys.stdin.readline())
    if num != 0: stack.append(num)
    else: stack.pop()
print(sum(stack))


# N = int(input()) # 이것은 별 차이 없음 
# stack = []
# for _ in range(N):
#     num = int(input()) # 여기서 sys를 안쓰면 시간이 오래걸림 4016ms , 위의 것은 80ms
#     if num > 0:
#         stack.append(num)
#     elif num == 0:
#         stack.pop()
        
# print(sum(stack))