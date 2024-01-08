# 첫째줄에 연산의 개수 n이 주어진다.
# 그 이후에 연산 정보 x가 자연수로 주어지면 배열에 자연수 x를 넣는다.

# x가 0이면 배열에서 가장 큰 값을 출력하고, 그 값을 배열에서 제거한다.
# 배열에 값이 없으면 0을 출력한다.

# 프로그램은 처음에 비어있는 배열에서 시작하게 된다.

import sys
import heapq
N = int(sys.stdin.readline())
arr = []
for _ in range(N):
    X = int(sys.stdin.readline())
    if X == 0:
        if len(arr) == 0:
            print(0)
        else:
            print(-heapq.heappop(arr))
    else:
        # 배열에 값 넣기
        heapq.heappush(arr, -X)