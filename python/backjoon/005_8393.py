import sys

n = int(sys.stdin.readline())
start = 1
sum = 0
while start <= n:
    sum += start
    start += 1
print(sum)
    