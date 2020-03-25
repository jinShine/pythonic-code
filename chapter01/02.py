# chapter01-02

# 객체지향 프로그래밍(OOP)
# * 클래스 상세 설명
# * 클래스 변수, 인스턴스 변수


# 클래스 선언
class Student():
    """
    Student Class
    Author: Jinnify
    Date: 2020.03.23
    """

    # 클래스 변수
    student_count = 0

    def __init__(self, name, number, grade, details, email=None):

        # self가 있는 인스턴스 변수들

        self.name = name
        self.number = number
        self.grade = grade
        self.details = details
        self.email = email

        Student.student_count += 1

    def __str__(self):
        return 'str {}'.format(self._name)

    def __repr__(self):
        return 'repr {}'.format(self._name)

    def detail_info(self):
        print('Current Id: {}'.format(id(self)))
        print('Current Id: {} {} {}'.format(self.name, self.email, self.details))

    def __del__(self):
        Student.student_count -= 1


# Self의 의미
student1 = Student("Cho", 2, 3, { 'gender': 'Male', 'score1' : 65, 'score2' : 44})
student2 = Student("Kim", 4, 1, { 'gender': 'Female', 'score1' : 85, 'score2' : 74})


# ID확인
# 서로 ID가 다르다.
print(id(student1))
print(id(student2))


# dir과 __dict__ 확인
print(dir(student1))
print(student2.__dict__)

# Docstring
print(student1.__doc__)

student1.detail_info()
student2.detail_info()
Student.detail_info(student1)
Student.detail_info(student2)


# 클래스 변수
print(Student.student_count)

# 클래스 변수의 공유 확인
print(Student.__dict__)
print(student1.__dict__)
print(student2.__dict__)

# 인스턴스 네임스페이스 없으면 상위에서 검색
# 즉, 동일한 이름으로 변수 생성 가능(인스턴스 검색 후 -> 상위(클래스 변수, 부모클래스 변수))


del student2

print(Student.student_count)