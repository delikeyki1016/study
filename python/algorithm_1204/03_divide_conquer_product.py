# 재귀와 분할정복, 그냥 재귀보다 반정도 횟수가 준다.
def divide_conquer_product(start, end):
    if end == start:
        return start
    if end == start + 1:
        return start * end
    else:
        print('호출')
        half = (start + end) // 2
        return divide_conquer_product(start, half) * divide_conquer_product(half + 1, end)
    
print(divide_conquer_product(1, 5))