import sys

N = int(sys.stdin.readline())
n_list = [int(i) for i in sys.stdin.readline().split()]
print(min(n_list), max(n_list))