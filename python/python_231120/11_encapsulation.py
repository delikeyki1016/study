import module.shape as s

rectangle1 = s.Rectangle(3,2)
rectangle2 = s.Rectangle(4,6)
print(rectangle1.get_perimeter())
print(rectangle2.get_perimeter())

cat = s.Cat()
dog = s.Dog()
person = s.Animal()

cat.sound()
dog.sound()
person.sound()