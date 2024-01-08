# 부분수열의 합
# arr 의 요소들의 합이 0이 되는 경우의 수 구하기 
import sys

# N, S = [int(i) for i in sys.stdin.readline().split()]
# arr = [int(i) for i in sys.stdin.readline().split()]
N, S = [5, 0]
arr = [-7, -3, -2, 5, 8]
count = 0
def dfs(idx, sum):
    global count
    if idx >= N:
        return
    sum += arr[idx]
    if sum == S:
        count += 1
    dfs(idx + 1, sum)
    dfs(idx + 1, sum - arr[idx])
dfs(0, 0)
print(count)