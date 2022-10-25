class Person:
		# 인스턴스 생성할 때 호출되는 함수 (생성자)
    def __init__(self, name, age):
				# 인스턴스 변수
        self.name = name
        self.age = age
		# 메서드 생성
    def speak(self):
        print(f'My name is {self.name}.')

# 인스턴스 생성
person1 = Person('David', 35)

# 인스턴스 활용
print(person1.name) # David
print(person1.age) # 35
person1.speak() # My name is David.