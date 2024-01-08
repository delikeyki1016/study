# https://www.acmicpc.net/problem/2164 카드
# deque (double ended queue): 스택과 큐를 합친 형태, 시간복잡도는 O(1), 슬라이싱 지원하지 않음 
# N장의 카드가 있다. 각각의 카드는 차례로 1부터 N까지의 번호가 붙어 있으며, 1번 카드가 제일 위에, N번 카드가 제일 아래인 상태로 순서대로 카드가 놓여 있다.
# 이제 다음과 같은 동작을 카드가 한 장 남을 때까지 반복하게 된다. 우선, 제일 위에 있는 카드를 바닥에 버린다. 
# 그 다음, 제일 위에 있는 카드를 제일 아래에 있는 카드 밑으로 옮긴다.
# 제일 마지막에 남게 되는 카드를 구하는 프로그램을 작성

import sys
from collections import deque

# N = int(sys.stdin.readline())
# queue = deque([i for i in range(1, N+1)])
# print(queue)
# while len(queue) > 1: 
#     queue.popleft()
#     # queue.append(queue.popleft())
#     queue.rotate(-1) # 위와 같음. 앞에 것을 빼서 뒤에 붙임 
#     print(queue)

# print(*queue) # print(queue.pop())과 같음 

# 시간초과 
# queue = [i for i in range(1, N+1)]
# print(queue)
# while len(queue) > 1: # != 1
#     queue.pop(0)
#     queue.append(queue.pop(0))
#     print(queue)
    
# print(queue[0])

# rotate 예시
nlist = deque([1,2,3,4,5])
nlist.rotate(-1)
print(nlist)
