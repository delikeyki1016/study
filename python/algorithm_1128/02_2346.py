# 풍선 터트리기
# 우선, 제일 처음에는 1번 풍선을 터뜨린다. 다음에는 풍선 안에 있는 종이를 꺼내어 그 종이에 적혀있는 값만큼 이동하여 다음 풍선을 터뜨린다. 
# 양수가 적혀 있을 경우에는 오른쪽으로, 음수가 적혀 있을 때는 왼쪽으로 이동한다. 이동할 때에는 이미 터진 풍선은 빼고 이동한다.

import sys
from collections import deque

# N = int(sys.stdin.readline())
balloon = deque(enumerate([int(i) for i in sys.stdin.readline().split()]))
print(balloon)
result = ''
while balloon:
    move = balloon.popleft()
    result += str(move[0] + 1) + ' '
    if move[1] > 0:
        balloon.rotate(-(move[1] - 1))
        print(balloon)
    else:
        balloon.rotate(-move[1])
        print(balloon)
        
print(result)
    
