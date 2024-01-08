import sys

N = int(sys.stdin.readline())
c = N // 4
if N % 4 != 0:
    c += 1
print("long " * c + 'int')