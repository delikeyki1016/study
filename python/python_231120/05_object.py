print(dir(object)) #object 클래스가 가진 속성들을 리스트로 반환

class Car: # 클래스를 생성하면 오브젝트가 가진 속성을 물려받고, 3개의 속성은 자동으로 추가된다.
    pass

print(dir(Car)) 

print(set(dir(Car)) - set(dir(object))) #{'__dict__', '__weakref__', '__module__'}

# 모듈은 변수와 함수를 모아놓은 것을 말합니다.
import math
print(math) #<module 'math' (built-in)> 내장되어있는 모듈 'math'
print(math.pi) # math 모듈에 있는 파이 변수 
print(math.sqrt(9)) # math 모듈에 있는 제곱근 구하는 함수

# 원의 둘레 공식 : pi * r*2  (r은 반지름)
# 원의 넓이 공식 : pi * r**2  (r은 반지름)

area = 78.53981633974483  # 넓이
print(f'반지름은 {math.sqrt(area/math.pi)}' )

# 주의사항 
from math import pi, sqrt # math모듈로 부터 pi, sqrt만 가져올께, 다른 모듈에서 pi, sqrt라는 함수를 가졌다면 동일이름으로 에러 가능성이 있다. 

print(pi, sqrt(9))