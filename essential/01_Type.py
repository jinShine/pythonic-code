#기본 출력
print('Hello Python!')

# --------------------------------------------------------------------------------
# format 사용
print('{} and {}'.format('You', 'Me'))
print('{0} and {1} and {0}'.format('You', 'Me'))
print('{var1} are {var2}'.format(var1='You', var2='Niceman'))

# --------------------------------------------------------------------------------
# 데이터 타입 종류

'''
int : 정수
float : 실수
complex : 복소수
bool : 불린

str : 문자열(시퀀스)
list : 리스트(시퀀스)
tuple : 튜플(시퀀스)
set : 집합
dict : 사전
'''

v_str1 = "NiceMan"
v_bool = True
v_float = 10.0
v_int = 7
v_list = [v_str1, v_bool]
v_dic = {
    "name" : "Jinnify",
    "age" : 30
}
v_tuple = 3, 5, 7
v_set = {7, 8, 9}

print(type(v_str1))
print(type(v_bool))
print(type(v_float))
print(type(v_int))
print(type(v_list))
print(type(v_dic))
print(type(v_tuple))
print(type(v_set))


# --------------------------------------------------------------------------------
# Numeric Operation (숫자형 연산자)

"""
+ 
- 
* 
/ 
// : 몫 
% : 나머지
abs(x) 
int(x) 
float(x) 
complex(x)
pow(x, y) 
x ** y : 제곱
....
"""