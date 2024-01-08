import sys

num1 = int(sys.stdin.readline())
num_list1 = set([int(i) for i in sys.stdin.readline().split()])
num2 = int(sys.stdin.readline())
num_list2 = [int(i) for i in sys.stdin.readline().split()]

for i in num_list2:
    if i in num_list1:
        print(1)
    else:
        print(0)