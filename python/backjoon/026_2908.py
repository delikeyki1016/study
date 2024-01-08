import sys

a, b = sys.stdin.readline().split()
# print(a[::-1])
print(max(int(a[::-1]), int(b[::-1])))
