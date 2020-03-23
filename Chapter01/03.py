# Chapter01-02

# 클래스 메서드, 인스턴스 메서드, Static 메서드

class Student(object):
    '''
    Student Class
    Author: Kim
    Date: 2020. 03. 23
    Description: Class, Static, Instance Method
    '''

    # 클래스 변수
    tuition_per = 1.0

    def __init__(self, id, first_name, last_name, email, grade, tuition, gpa):

        # 인스턴스 변수
        self._id = id
        self._first_name = first_name
        self._last_name = last_name
        self._email = email
        self._grade = grade
        self._tuition = tuition
        self._gpa = gpa

    # 인스턴스 메서드
    def full_name(self):
        return '{}, {}'.format(self._first_name, self._last_name)

    # 인스턴스 메서드
    def detail_info(self):
        return 'Student Detail Info : {},{},{},{},{},{}'.format(self._id, self.full_name(), self._email, self._grade, self._tuition, self._gpa)

    # 인스턴스 메서드
    def get_fee(self):
        return 'Before Tuition -> Id : {}, fee : {}'.format(self._id, self._tuition)

    # 인스턴스 메서드
    def get_free_culc(self):
        return 'After tuition -> Id : {}, fee : {}'.format(self._id, self._tuition * Student.tuition_per)

    # 인스턴스 메서드
    def __str__(self):
        return 'Student Info -> name : {}, grade : {}, email : {}'.format(self.full_name(), self._grade, self._email)

    # 클래스 메서드
    @classmethod
    def raise_fee(cls, per):
        if per <= 1:
            print("Please Enter 1 or More")
            return

        # cls는 자기 자신의 클래스를 의미한다. 즉, Student
        cls.tuition_per = per
        print('Succed! tuition increased')

    # 클래스 메서드
    # 보통 __init__으로 생성해서 초기값을 생성하기 보다는
    # 클래스 메서드를 만들어서 생성하는 방법을 권장한다(파이토닉!)
    @classmethod
    def student_const(cls, id, first_name, last_name, email, grade, tuition, gpa):
        return cls(id, first_name, last_name, email, grade, tuition * cls.tuition_per, gpa)




student_1 = Student(1, 'Kim', 'Sarang', 'student1@naver.com', '1', 400, 3.5)
student_2 = Student(2, 'Park', 'Jin', 'student2@daum.com', '2', 500, 4.0)

# __str__이 호출된다.
print(student_1)
print(student_2)

print()

# 전체 정보
print(student_1.detail_info())
print(student_2.detail_info())

print()

# 학비 정보
print(student_1.get_fee())
print(student_2.get_fee())

# 학비 인상(클래스 메서드 미 적용)
# 클래스 변수를 직접적으로 접근해서 값을 변경하는것은 안좋다!
# 클래스 메서드를 만들어 변경하는 방법을 알아보자!
Student.tuition_per = 1.2

# 학비 정보(인상 후)
print(student_1.get_free_culc())
print(student_2.get_free_culc())

# 클래스 변수를 직접적으로 접근해서 값을 변경하는것은 안좋다!
# 클래스 메서드를 만들어 변경하는 방법을 알아보자!

# 클래스 메서드
Student.raise_fee(1.5)

# 학비 정보(인상 후)
print(student_1.get_free_culc())
print(student_2.get_free_culc())

# 클래스 메서드 인스턴스 생성 실습
student_3 = Student.student_const(3, 'Kim', 'Jinnify', 'seungjin@naver.com', '3', 550, 4.5)
student_4 = Student.student_const(4, 'Cho', 'han', 'han22@naver.com', '4', 800, 4.0)

print(student_3.detail_info())
print(student_4.detail_info())

# 학생 학비 변경 확인
print(student_3)

def is_scholarship(inst):
    if inst._gpa >= 4.3:
        return '{} is a scholarship recipient'.format(inst._last_name)
    return 'Sorry not a scholarship recipient'

print(is_scholarship(student_1))
print(is_scholarship(student_2))
print(is_scholarship(student_3))
print(is_scholarship(student_4))