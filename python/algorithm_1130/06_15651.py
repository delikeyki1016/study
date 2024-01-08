# 자연수 N,M -> N으로 1~ 리스트를 만들어서, M자리수의 경우의 수를 리턴
import sys

N, M = [int(i) for i in sys.stdin.readline().split()]
nums = [i for i in range(1, N+1)]

def dfs(path):
    if len(path) == M:
        print(*path)
        return 
    for i in nums:
        path.append(i)
        dfs(path)
        path.pop()
        print('pop path', path)
dfs([])

# import itertools
# results = itertools.product(nums, repeat=M)
# for i in results:
#     print(*i)