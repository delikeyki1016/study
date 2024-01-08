# 객체 지향 이론 - 캡슐화
class Rectangle:
    # 가로의 길이가 같다. 세로의 길이가 같다.
    def __init__(self, width, height):
        self.width = width
        self.height = height
        
    def get_perimeter(self):
        return 2 * (self.__get_width_plus_height__())
    
    def __get_width_plus_height__(self): # private method (캡슐화)
        return self.width + self.height
    

# 객체 지향 이론 - 다형성 => Overriding
class Animal:
    def sound(self):
        print('동물의 소리입니다.')
        
        
class Cat(Animal):
    def sound(self):
        print('야옹~')
        

class Dog(Animal):
    def sound(self):
        print('멍멍~')