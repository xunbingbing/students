import json

student_list = []

class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def __str__(self):
        return f"姓名：{self.name} 成绩：{self.score}"

def load_data():
    try:
        with open("students.json", "r", encoding="utf-8") as f:
            data_from_file = json.load(f)
            student_list = []
            for item in data_from_file:
                student_list.append(Student(item["name"], item["score"]))
    except FileNotFoundError:
        student_list = []
    return student_list

def save_data(student_list):
    data_to_save = []
    for student in student_list:
        data_to_save.append({"name": student.name, "score": student.score})
    with open("students.json", "w", encoding="utf-8") as f:
        json.dump(data_to_save, f, ensure_ascii=False, indent=4)

def add_student(student_list):
    try:
        name = input("请输入学生姓名：")
        score = int(input("请输入学生成绩："))
    except (ValueError, TypeError):
        print("输入无效，请重新输入")
        return
    student_list.append(Student(name, score))

def show_students(student_list):
    if len(student_list) == 0:
        print("暂无学生")
    else:
        for student in student_list:
            print(f"{student.name}的成绩是{student.score}")

def delete_student(student_list):
    name = input("请输入要删除的学生姓名：")
    original_len = len(student_list)
    student_list[:] = [s for s in student_list if s.name != name]
    if len(student_list) < original_len:
        print(f"已删除学生：{name}")
        save_data(student_list)
    else:
        print(f"未找到学生：{name}")

def calculate_average(student_list):
    if len(student_list) == 0:
        print("暂无学生")
    else:
        total = 0
        for student in student_list:
            total += student.score
        average = total / len(student_list)
        print(f"总成绩为：{total}，平均成绩为：{average}")

def find_student(student_list):
    name = input("请输入要查找的学生姓名：")
    for student in student_list:
        if student.name == name:
            print(f"找到学生：{student.name}，成绩：{student.score}")
            return
    print(f"未找到学生：{name}")

def updata_student(student_list):
    name = input("请输入要修改成绩的学生姓名：")
    for student in student_list:
        if student.name == name:
            try:
                new_score = int(input(f"请输入{student.name}的新成绩："))
                student.score = new_score
                print(f"{student.name}的成绩已更新为：{student.score}")
                save_data(student_list)
                return
            except (ValueError, TypeError):
                print("输入无效，请重新输入")
    print(f"未找到学生：{name}")
