# 미로탐색
import sys
from collections import deque

# N, M = [int(i) for i in sys.stdin.readline().split()]
# maze = [[int(i) for i in sys.stdin.readline().rstrip()] for _ in range(N)]
N, M = [4, 6]
maze = [
    [1, 0, 1, 1, 1, 1],
    [1, 0, 1, 0, 1, 0],
    [1, 0, 1, 0, 1, 1],
    [1, 1, 1, 0, 1, 1]
]

queue = deque()
queue.append([0, 0])# 시작 위치

direction = [(0, -1), (0, 1), (-1, 0), (1, 0)] # 상하좌우

def bfs():
    while queue:
        x, y = queue.popleft()
        for i in direction:
            new_x = x + i[0]
            new_y = y + i[1]
            if 0 <= new_x < M and 0 <= new_y < N:
                if maze[new_y][new_x] == 1:
                    maze[new_y][new_x] = maze[y][x] + 1
                    queue.append([new_x, new_y])
    maze[0][0] = 1
    print(maze)

bfs()
print(maze[N-1][M-1])