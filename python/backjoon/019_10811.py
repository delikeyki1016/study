import sys
basket, change = map(int, sys.stdin.readline().split())
basket = [i for i in range(1, basket + 1)]
for _ in range(change):
    start, end = map(int, sys.stdin.readline().split())
    temp = basket[start-1:end]
    # print('temp', temp)
    temp.reverse()
    # print('temp reverse', temp)
    basket[start-1:end] = temp
    # print('basket',basket)

print(*basket)