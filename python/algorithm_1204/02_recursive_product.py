def recursive_product(start, end):
    if end == start + 1:
        return end * start
    else:
        print('호출')
        return end * recursive_product(start, end - 1)
    
print(recursive_product(1, 5))