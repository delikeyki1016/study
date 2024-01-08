# 빈집합에 명령과 값을 입력받아, 명령에 해당하는 조건문을 찾아 명령을 수행, check는 그 수가 존재하면 1, 없으면 0 출력
# all은 집합에 1~20까지 값 넣기 

import sys # 시간초과 이슈가 있어요!!!

S = set()
calc_count = int(sys.stdin.readline())
# calc_count = int(input()) # 시간초과 이슈로 import sys, sys.stdin.readLine() 사용  

for _ in range(calc_count) :
    cmd = sys.stdin.readline().split()
    if len(cmd) > 1 and cmd[1] in cmd :
        cmd[1] = int(cmd[1])
    
    if cmd[0] == 'add' :
        S.add(cmd[1])
    elif cmd[0] == 'remove' :
        S.discard(cmd[1]) # 없을때 지우려면 에러를 내는데, discard는 있을때만 지움 
    elif cmd[0] == 'check' :
        if cmd[1] in S : print(1)
        else : print(0)
    elif cmd[0] == 'toggle' :
        if cmd[1] in S : S.remove(cmd[1])
        else : S.add(cmd[1])
    elif cmd[0] == 'all' :
        S = set([i for i in range(1, 20+1)])
    elif cmd[0] == 'empty' :
        S.clear()