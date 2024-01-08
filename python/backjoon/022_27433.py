# num = int(input())
# def factorial(n):
#     if n == 0: # 0! = 1 이다
#         return 1
#     return n * factorial(n-1)
# print(factorial(num))

# x의 n제곱 구하기
x = int(input())
n = int(input())
def double(x, n):
    if n == 0: 
        return 1
    return x * double(x, n-1)
print(double(x, n))
