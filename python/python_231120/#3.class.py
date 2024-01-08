class Animal:
    # 클래스 변수
    age = 1
    # 클래스 함수
    # def set_name(self, data): 
    #     self.name = data 
    def info(self):
        print(f'안녕하세요 저는 {self.name}입니다. {self.age}살입니다.')
    # 생성자(__init__) : 객체를 생성할 때 가장 먼저 호출되는 함수, 즉 객체를 생성하면 __init__ 함수가 자동으로 실행되어 생성된다.
    def __init__(self):
        self.name = 'unnamed'
        self.age = -1
    # 인스턴스 함수 

pig = Animal()
# print(pig, type(pig)) # <__main__.Animal object at 0x00000270F1D31CA0>  0x00000270F1D31CA0 는  메모리 주소,  <class '__main__.Animal'>
# pig.set_name("꿀꿀이")
# pig.info()

# 상속
class Human(Animal): # Human이 Animal(부모)의 특성을 상속받음, Human의 생성자는 Animal의 생성자를 상속받음 
    def __init__(self):
        self.job = "student"
        super().__init__() # 반드시 부모 생성자를 호출해야함 필수! 
    def speak(self, data):
        print(f'{self.name}은 \"{data}\"라고 말을 합니다.')
    def info(self): # 자식클래스에서 재정의해서 사용.오버라이딩(overriding)
        print(f'안녕하세요 저는 {self.name}입니다. {self.age}살이고, 직업은 {self.job} 이에요')

hong = Human()
hong.name = "홍길동"
hong.age = 20
hong.speak("hello")
hong.info()

# 내장변수,내장함수 (스페셜메소드) __init__ : 특정상황에서 자동으로 호출됨 ex) __len__, __str__
class Car:
    def __init__(self, data):
        self.id = data # Car(1234) 로 입력했을때는 str(data)
    
    def __len__(self):
        return len(self.id)
    
    def __str__(self): # 파이썬에서 print 함수를 사용하여 객체를 출력하면 기본적으로 해당 객체의 __str__ 메서드가 호출
        return "차 번호:" + self.id
    
def main():
    c = Car('125678')
    print(c)
    print(len(c))
    print(str(c))

main()