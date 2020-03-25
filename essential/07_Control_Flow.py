# 파이썬 흐름제어(제어문)
# 조건문 실습

# 기본 형식

# 예1
if True:
    print("Yes")  # 들여쓰기 중요

if False:
    # 출력되지 않음.
    print("No")

# 예2
if False:
    # 여기는 실행되지 않음.
    print("You can't reach here")
else:
    # 여기가 실행된다.
    print("Oh, you are here")



# 관계연산자
# >, >=, <, <=, ==, !=

# 논리연산자
# and, or, not

a = 100
b = 60
c = 15

print(a > b and b > c)

if a != 1:
    print("OK")

if not a != 100:
    print("100이 아니다!")


# 다중 조건문
num = 90

if num >= 70:
    print("num ? ", num)
elif num >= 60:
    print("num ? ", num)
else:
    print("default num")

# 중첩 조건문

age = 27
height = 175

if age >= 20:
    if height >= 170:
        print("A지망 지원 가능")
    elif height >= 160:
        print("B지망 지원 가능")
    else:
        print("지원 불가")
else:
    print("20세 이상 지원가능")

# in, not in

q = [1, 2, 3]
w = {7, 8, 9, 9}
e = {"name": 'Kim', "city": "seoul", "grade": "B"}
r = (10, 12, 14)

print(1 in q)
print(6 in w)
print(12 not in r)
print("name" in e)  # key 검색
print("seoul" in e.values())  # value 검색



st_name = "Goodboy"
print(reversed(st_name))

for c in reversed(st_name):
    print(c)

q3 = ["갑", "을", "병", "정"]
print([s for s in q3 if s != '정']) # [값, 을, 병]
print(''.join([s for s in q3 if s != '정'])) # 값을병

def func_mul1(x):
    y1 = x * 2
    y2 = x * 4
    y3 = x * 6
    return y1, y2, y3


val1, val2, val3 = func_mul1(3)

print(val1, val2, val3)