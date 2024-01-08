# isinstance는 객체가 어떤 클래스의 인스턴스인지 알려주는 함수

class Car:
    def __init__(self, data):
        self.id = data

c = Car('12가5678')
print(c.id) # 12가5678
print(isinstance(c, Car))
print(isinstance('abc', str))
print(isinstance(123, int)) 
print(isinstance(123, object))   # 모든 자료의 최상위 클래스는 object이다. 파이썬은 객체다.