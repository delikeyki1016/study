# 피보나치
# 피보나치 수는 0과 1로 시작한다. 0번째 피보나치 수는 0이고, 1번째 피보나치 수는 1이다. 
# 그 다음 2번째 부터는 바로 앞 두 피보나치 수의 합이 된다.
# 이를 식으로 써보면 Fn = Fn-1 + Fn-2 (n ≥ 2)가 된다.
# num = int(input())

# def pivo(n):
#     if n <= 1: # n이 0일때는 0, n이 1일때는 1이므로 n<=1 일때는 n을 반환
#         return n
#     return pivo(n - 1) + pivo(n - 2) # 피보나치 수는 앞의 두 피보나치 수의 합이다. 따라서, n번째 피보나치 수는 (n-1)과 (n-2)의 합이 된다.
# print(pivo(num))


def pivo(n):
    c_0 = 0
    c_1 = 0
    if n == 1:
        c_1 += 1
        return 1 
    if n == 0:
        c_0 += 1
        return 0
    pivo(n - 1) + pivo(n - 2)
    result = [c_0, c_1]
    return result
    
import sys 
T = int(sys.stdin.readline())
for _ in range(T):
    n = int(sys.stdin.readline())
    print(pivo(n))
    