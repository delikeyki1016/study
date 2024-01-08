for i in range(1, 11) :
    print(f"{i}: kang")
    
x = 11
while x <= 20 :
    print(f'{x}: kang')
    x += 1
    
# range(start, stop, 증가수) 
# range 함수는 반복 객체(제너레이터)를 반환 => 메모리 소모가 적다.
print(list(range(10)))
print(list(range(1, 10+1)))
print(list(range(1, 10+1, 3)))