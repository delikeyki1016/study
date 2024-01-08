# https://www.acmicpc.net/problem/18258  queue = [] 로 사용하면 시간초과 가 뜬다. 그래서 deque 사용 

import sys
from collections import deque 

N = int(sys.stdin.readline())
queue = deque()
# queue = [] => queue = deque()
# queue.pop(0) => queue.popleft()

for _ in range(N):
    cmd, *num = sys.stdin.readline().split()
    
    if cmd == 'push':
        queue.append(int(*num))
    elif cmd == 'pop':
        if queue: print(queue.popleft())
        else: print(-1)
    elif cmd == 'size':
        print(len(queue))
    elif cmd == 'empty':
        # 큐가 비어있으면 1, 아니면 0을 출력한다.
        print(int(queue == deque([])))
        # print(int(bool(not queue)))
    elif cmd == 'front':
        if queue: print(queue[0])
        else: print(-1)
    elif cmd == 'back':
        if queue: print(queue[-1])
        else: print(-1)