# https://www.acmicpc.net/problem/10828
# 스택을 list를 이용해서 풀기

import sys
N = int(sys.stdin.readline())
stack_list = []

for i in range(N):
    cmd, *num = sys.stdin.readline().split()
    if cmd == 'push':
        stack_list.append(int(*num))
    elif cmd == 'pop':
        if stack_list: print(stack_list.pop())
        else: print(-1)
    elif cmd == 'size':
        print(len(stack_list))
    elif cmd == 'empty':
        # if stack_list: print(0)
        # else: print(1)
        print(int(stack_list == []))
    elif cmd == 'top':
        if stack_list: print(stack_list[-1])
        else: print(-1)


    