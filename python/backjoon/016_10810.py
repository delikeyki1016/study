import sys
N, M = sys.stdin.readline().split()
basket = [0] * int(N)

for _ in range(int(M)):
    bs, be, num = [int(i) for i in sys.stdin.readline().split()]
    while bs <= be:
        basket[bs - 1] = num
        bs += 1
    
# for i in range(int(N)):
#     print(basket[i], end=" ")
print(*basket)
