# Class : 현실세계의 사물을 컴퓨터 안에서 구현하려고 고안된 개념
# 클래스 = 속성(정적특징, 변수라고 부르지않고 "필드field"라 부름) + 메서드(동적특징, 함수라 부르지않고 "method메서드"라 부름)
# 붕어빵틀 => 클래스(부모), 붕어빵s => 인스턴스(자식) ex) 붕어빵1 = 붕어빵틀() => 인스턴스명 = 클래스명()
# self.속성명(필드) => self가 this
class Car : # 1.클래스선언
    #속성(필드)
    color = ""
    speed = 0
    #메서드
    def upSpeed(self, value) : 
        self.speed += value
    def downSpeed(self, value) :
        self.speed -= value
          
myCar1 = Car()  # 2. 인스턴스 생성
myCar1.color = "빨강" # 3. 필드나 메서드 사용
myCar1.speed = 0
print("myCar1=>", "color:", myCar1.color, "speed:", myCar1.speed)
myCar1.upSpeed(30)
print("myCar1 speed:", myCar1.speed)
myCar1.downSpeed(10)
print("myCar1 speed:", myCar1.speed)

##생성자(Constructor) : 인스턴스를 생성하면 무조건 호출되는 메서드, 인스턴스를 생성하면서 필드값(속성)을 초기화시키는 함수
class Car2 :
    color = ""
    speed = 0
    def __init__(self) : #생성자
        self.color = "빨강"
        self.speed = 0

myCar2 = Car2()
print("Car2의 색상은 %s이며, 현재 속도는 %dKm입니다." % (myCar2.color, myCar2.speed))

class Car3 :
    color = "" #인스턴스 변수(인스턴스 내에 독립적으로 저장된 독립변수)
    speed = 0  #인스턴스 변수
    def __init__(self, value1, value2) : #생성자
        self.color = value1
        self.speed = value2

myCar3 = Car3("파랑", 40)
print("Car3의 색상은 %s이며, 현재 속도는 %dKm입니다." % (myCar3.color, myCar3.speed))      


## 인스턴스 변수, 클래스 변수 
# 인스턴스 변수는 인스턴스 개별로 가지고 있는 독립변수이고, 클래스 변수는 클래스 안에 공간이 할당되는 변수 
# 예를들어 Car클래스에 클래스변수로 수량변수를 선언하면, 인스턴스들도 수량변수를 공유한다. 
# 사용은 클래스명.클래스변수 or 인스턴스명.클래스변수 (둘다 가능) 변수를 공유한다면 클래스변수로 사용하면 된다.
class Car4 :
    speed = 0
    count = 0 
    def __init__(self, speed) :
        self.speed = speed
        Car4.count += 1
        
myCar4 = Car4(50)
print("myCar4의 현재속도는 %dkm이고, 생산된 자동차는 %d대 입니다." % (myCar4.speed, Car4.count))
myCar5 = Car4(80)
print("myCar5의 현재속도는 %dkm이고, 생산된 자동차는 %d대 입니다." % (myCar5.speed, myCar5.count))

## 클래스의 상속(Inheritance) 
# 부모클래스(슈퍼클래스)에게 상속받은 후에는 자식클래스(서브클래스)에서 추가로 필드나 메서드를 만들어 사용 가능 => 오버라이딩(Overriding) 즉 재정의
# 선언형식
# class 서브_클래스(슈퍼_클래스) :
class Car6 :
    speed = 0
    
    def upSpeed(self, value) :
        self.speed += value
        print("현재속도(슈퍼클래스): %d" % self.speed)

class Sedan(Car6) :
    seat = 0 
    def upSpeed(self, value) :
        self.speed += value
        if self.speed > 150 :
           self.speed = 150
        print("현재속도(서브클래스): %d" % self.speed)

    def getSeat(self, value) :
        self.seat += value
        print("좌석수 : %d" % self.seat)

# class Truck(Car6) :
#     pass #부모클래스를 그대로 사용

class Truck(Car6) :
    load = 0
    def getLoad(self, value) :
        self.load += value
        print("적재량 : %d톤" % self.load)

sedan1 = Sedan()
truck1 = Truck()

print("==세단==")
print("세단 => ", end="") # end="" 는 개행하지 않고 이어줌 
sedan1.upSpeed(200)
sedan1.getSeat(4)
print("==트럭==")
print("트럭 => ", end="")
truck1.upSpeed(200)
truck1.getLoad(25)




