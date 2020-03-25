# 클래스, 인스턴스 차이 중요
# 네임스페이스 : 객체를 인스턴스화 할 때 저장된 공간
# 클래스 변수 : 직접 사용 가능, 객체보다 먼저 생성
# 인스턴스 변수 : 객체마다 별도로 존재, 인스턴스 생성 후 사용

# 예제1

class UserInfo:
    def __init__(self, name):
        self.name = name

    def print_info(self):
        print("Name: " + self.name)

    @classmethod
    def init(cls, name, age):
        cls(name, age)

    def __del__(self):
        print("Instance removed!")


user1 = UserInfo("Kim")
user2 = UserInfo("Park")


print(id(user1))
print(id(user2))

user1.print_info()
user2.print_info()

print('user1 : ', user1.__dict__)  # 클래스 네임스페이스 확인
print('user2 : ', user2.__dict__)

print(user1.name)


# 예제2
# self의 이해

class SelfTest:

    def function2(self):
        print(id(self))
        print("function2 called!")


f = SelfTest()
# print(dir(f))
print(id(f))
# f.function1() #예외 발생
f.function2()



# print(SelfTest.function2()) #예외 발생


# 예제3
# 클래스 변수 , 인스턴스 변수

class Warehouse:
    # 클래스 변수
    stock_num = 0

    def __init__(self, name):
        # 인스턴스 변수
        self.name = name
        Warehouse.stock_num += 1

    def __del__(self):
        Warehouse.stock_num -= 1


user1 = Warehouse('Kim')
user2 = Warehouse('Park')

print(user1.name)
print(user2.name)
print(user1.__dict__)
print(user2.__dict__)
print(Warehouse.__dict__)  # 클래스 네임스페이스 , 클래스 변수 (공유)

# Warehouse.stock_num = 50 # 직접 접근 가능

print(user1.stock_num)
print(user2.stock_num)

# ----------------------------------------
# 파이썬 클래스 상세 이해
# 상속, 다중상속

class Car:
    def __init__(self, type, color):
        self._type = type
        self._color = color

    def show(self):
        return 'Car 뼈대'


class BmwCar(Car):
    def __init__(self, type, color, name):
        super().__init__(type, color)
        self._name = name

    def show(self):
        return 'Your Car name {}'.format(self._name)

class BenzCar(Car):
    def __init__(self, type, color, name):
        super().__init__(type, color)
        self._name = name

    def show(self):
        return 'Your Car name {}'.format(self._name)

carModel = BmwCar('sedan', 'black', '520d')
print(carModel._color) # super
print(carModel._type) # super
print(carModel._name) # sub


# 다중 상속
class X():
    pass

class Y():
    pass

class Z():
    pass

class A(X, Y, Z):
    pass

print(A.mro())

