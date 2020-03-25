# chapter01-01

# 객체지향 프로그래밍(OOP)
# * 클래스 상세 설명
# * 클래스 변수, 인스턴스 변수

# ---------------------------------------------------------
# 아래와 같이 코드 절차지향으로 코드를 생성했다고 했을때
# 학생 100명이 있다고 가정하면 많은 소스들이 필요하며 관리가 힘들겠죠.


# 학생 1
student_name_1 = "Kim"
student_number_1 = 1
student_grade_1 = 1
student_detail_1 = [
    {'gender' : 'Male'},
    {'score1' : '95'},
    {'score2' : '99'},
]

# 학생 2
student_name_2 = "Lee"
student_number_2 = 2
student_grade_2 = 2
student_detail_2 = [
    {'gender' : 'Female'},
    {'score1' : '79'},
    {'score2' : '87'},
]

# 학생 3
student_name_3 = "Park"
student_number_3 = 3
student_grade_3 = 3
student_detail_3 = [
    {'gender' : 'Male'},
    {'score1' : '85'},
    {'score2' : '88'},
]


# 리스트 구조
student_names_list = ['Kim', 'Lee', 'Park']
student_numbers_list = [1, 2, 3]
student_grades_list = [1, 2, 3]
student_details_list = [
    {'gender': 'Male', 'score1': '95', 'score2': '99'},
    {'gender': 'Female', 'score1': '79', 'score2': '87'},
    {'gender': 'Male', 'score1': '85', 'score2': '88'}
]

# 학생 삭제
del student_names_list[1]
del student_numbers_list[1]
del student_grades_list[1]
del student_details_list[1]

print(student_names_list)
print(student_numbers_list)
print(student_grades_list)
print(student_details_list)


print()
print()

# ---------------------------------------------------------

# 딕셔너리 구조
students_dicts = [
    {'student_name': 'Kim', 'student_number': 1, 'student_grade': 1, 'student_detail': {'gender': 'Male', 'score1': 95, 'score2': 99}},
    {'student_name': 'Lee', 'student_number': 2, 'student_grade': 2, 'student_detail': {'gender': 'Female', 'score1': 79, 'score2': 87}},
    {'student_name': 'Park', 'student_number': 3, 'student_grade': 3, 'student_detail': {'gender': 'Male', 'score1': 85, 'score2': 88}}
]

del students_dicts[1]
print(students_dicts)


# ---------------------------------------------------------
# 여전히 인덱스로 접근하고 있고, 100명을 추가한다고할때도 여전히 중복코드와 많이 불편하다

# 클래스 구조
class Student():
    def __init__(self, name, number, grade, details):
        self.name = name
        self.number = number
        self.grade = grade
        self.detail = details

    # 인스턴스가 불릴때 오버라이드한 __str__을 불러 커스텀으로 출력 가능
    def __str__(self):
        return 'str : {}'.format(self.name)

    def __repr__(self):
        return 'repr : {}'.format(self.name)

student1 = Student("Kim", 1, 1, {'gender': 'Male', 'score1': 95, 'score2': 99})
student2 = Student("Lee", 2, 2, {'gender': 'Female', 'score1': 79, 'score2': 87})
student3 = Student("Park", 3, 3, {'gender': 'Male', 'score1': 85, 'score2': 88})

# __dict__ -> 생성자로 넘긴 데이터들을 다 확인 할 수 있다.
print(student1.__dict__)
print(student2.__dict__)
print(student3.__dict__)

# 리스트 선언
students_list = []

students_list.append(student1)
students_list.append(student2)
students_list.append(student3)

for student in students_list:
    print(student)
