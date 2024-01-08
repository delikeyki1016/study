# def recursion_sum(num):
#     if num == 1:
#         return 1
#     result = recursion_sum(num - 1)
#     return num + result

# print(recursion_sum(5))


# 팩토리얼 (factorial)
# import sys

# def factorial(num):
#     if num == 0:
#         return 1
#     result = factorial(num - 1)
#     return num * result

# number = int(sys.stdin.readline())
# print(factorial(number))

def add_num(num):
    if num == 1:
        return 1 
    return num + add_num(num-1)

print(add_num(5))