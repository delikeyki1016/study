import sys

N = int(sys.stdin.readline())
m_list = [int(i) for i in sys.stdin.readline().split()]
v = int(sys.stdin.readline())
num = 0
for i in m_list:
    if i == v:
        num += 1
print(num)