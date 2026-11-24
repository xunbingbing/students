# import random

# a = random.randint(1,100)
# c = 0
# while True:
#     b = int(input("a number: "))
#     c += 1
    
#     if b == a:
#         print(f"You win! 一共猜了{c}次")
#         break
#     elif b > a:
#         print("大了")
#     elif b < a:
#         print("小了")


# null_py_book = 99.80
# vip_book = 77.80
# fan_vip_book = 76.80
# plus_vip_book = 75.80
# vip_type = input("请输入会员类型：")
# quantity = int(input("请输入购买数量："))
# discount = 0
# cashback = 0
# if vip_type == "null":
#     total = null_py_book * quantity
#     print(f"{quantity}件商品，应付金额：{total}元")
# elif vip_type == "vip":
#     total = vip_book * quantity
#     print(f"{quantity}件商品，应付金额：{total}元")
# elif vip_type == "fan_vip":
#     total = fan_vip_book * quantity
#     print(f"{quantity}件商品，应付金额：{total}元")
# elif vip_type == "plus_vip":
#     total = plus_vip_book * quantity
#     print(f"{quantity}件商品，应付金额：{total}元")
# else:
#     print("会员类型输入错误")
# if total > 49:
#     shipping_fee = 0
#     print("运费：0元")
# else:
#     shipping_fee = 6
#     print("运费：6元")
# if total >= 299:
#     print("优惠金额：-15元")
#     discount = 15
# elif total >= 149:
#     print("优惠金额：-5元")
#     discount = 5
# cashback = (total // 100) * 50
# if cashback > 0:
#     print(f"返现：{cashback}元")
# price = total-cashback-discount+shipping_fee
# print(f"总金额：{price}元")

# name = input("请输入名字：")
# age = int(input("请输入年龄："))
# year = int(input("请输入年份："))
# print(f"你好，{name},你今年{age}岁，距离28年毕业还有{28 - year}年")

# x = float(input("任意小数："))
# print(f"{x:.2f}")

# day = int(input("请输入天数(1-7)："))
# if day == 1:
#     print("星期一")
# elif day == 2:
#     print("星期二")
# elif day == 3:
#     print("星期三")
# elif day == 4:
#     print("星期四")
# elif day == 5:
#     print("星期五")
# elif day == 6:
#     print("星期六")
# elif day == 7:
#     print("星期日")
# else:
#     print("输入错误")

# text = input("输入任意字符：")
# print(text.strip().title()) 

# i = 1
# total = 0
# num = int(input("请输入一个整数："))
# while i <= num:
#     total += i
#     i += 1
# print(f"1到{num}的和为：{total}")

# num = int(input("请输入一个整数："))
#i = 1
# while i <= num:
#     if i % 3 == 0:
#         print(f"{i}是3的倍数")
#     else:
#         print(f"{i}不是3的倍数")
#     i += 1
        
# num = "10"
# for i in num:
#     print(i)

# n = int(input("请输入一个整数："))
# i = 1
# num = 1
# while i <= n:
#     num *= i
#     i += 1
# print(f"{n}的阶乘为：{num}")

# password = input("请输入密码：")
# if password == "123456":
#     print("密码正确,登录成功")
# else:
#     print("密码错误,请重新输入")
# while True:
#     password = input("请输入密码：")
#     if password == "123456":
#         print("密码正确,登录成功")
#         break
#     else:
#         print("密码错误,请重新输入")
        
# n = int(input("请输入一个整数："))
# num = 1
# while num <= n:
#     if num % 2 == 0:
#         print(f"{num}是偶数")
#     num += 1

# n = int(input("请输入一个整数："))
# num = n
# while num >= 1:
#     print(f"{num}")
#     num -= 1
# print("发射")

# num = int(input("请输入一个整数："))
# while num > 0:
#     i = num % 10
#     print(i)
#     num //= 10

#第150行到第158行代码为逻辑灾难，需要重写
# target = int(input("请输入目标金额："))
# total = 0
# while True:
#     money = int(input("请输入金额："))
#     total += money
#     if total > target:
#         print(f"目标达成，总计{total}元")
#     else:
#         input("请输入一笔金额:")
#     break

# target = int(input("请输入目标金额："))
# total = 0
# while total < target:
#     money = int(input("请输入金额："))
#     total += money
#     print(f"当前总计{total}元")
# print(f"目标达成，总计{total}元")

# n = int(input("请输入一个整数："))
# for i in range(1,n+1):
#     if i % 2 == 0:
#         print(f"{i}是偶数")

# shopping_cart = []
# while True:
#     item = input("请输入商品名称(输入q退出)：")
#     if item == "q":
#         break
#     shopping_cart.append(item)
# print(f"购物车中的商品有：{shopping_cart}")
# print(f"商品数量：{len(shopping_cart)}")

# scores = [85, 90, 78, 92, 88]
# total = 0
# for score in scores:
#     total += score
# print(f"总分：{total}")

# scores = [85, 90, 78, 92, 88]
# for score in scores:
#     if score >= 90:
#         print(score)

# for i in range(1,11):
#     if i == 7:
#         print(f"找到{i}了，停止")
#         break

# names = ["张三","李四","王五"]
# for i in range(len(names)):
#     print(names[i])
#     i += 1    #无用代码，for循环里不需要自增

# s = [1,2,3,4,5,6,7,8,9]
# print(s[1:4:1])

# prices = {"苹果":5.5,"香蕉":3.2,"橘子":4.0}
# for key,value in prices:     #只使用了key，导致不能输出价格value
#     print(f"{key}的价格为{value}")     #最开始为price["苹果"]，只能输出苹果的价格
#     break

# prices = {"苹果":5.5,"香蕉":3.2,"橘子":4.0}
# fruit = input("请输入水果名称：")
# if fruit in prices:
#     print(f"{fruit}的价格是{prices[fruit]}元。")     #print输出拼写为prices
# else:
#     print("抱歉，没有这个水果。")

# users = [
#     {"name": "张三", "age": 20, "vip": True},
#     {"name": "李四", "age": 25, "vip": False},
#     {"name": "王五", "age": 22, "vip": True}
# ]
# for user in users:
#     if user["vip"] == True:     #True拼写错误
#         print(f"vip用户姓名为：{users["name"]}")

# def say_hallo():
#     print("欢迎学习 Python!")
# say_hallo()

# def calculate_area(length,width):
#     area_ = length * width
#     return area_
# area_1 = calculate_area(5,3)
# print(area_1)

# users = [
#     {"name": "张三", "age": 20, "vip": True},
#     {"name": "李四", "age": 25, "vip": False},
#     {"name": "王五", "age": 22, "vip": True}
# ]
# def check_vip(user):
#         if user["vip"] == True:
#             print("尊贵的VIP用户")
#         else:
#             print("普通用户")
# for user in users:
#     print(check_vip(user))

# 对第243行至第249行修正
# def check_vip(user):
#     if user["vip"] == True:
#         return "尊贵的VIP用户"
#     else:
#         return "普通用户"
# for user in users:
#     status = check_vip(user)
#     print(f"用户：{users['name']}，身份：{status}")
        
# num1 = int(input("请输入第一个数字："))

# try:
#     num2 = int(input("请输入第二个数字："))
#     print(f"{num1/num2}")
# except Exception as e:  
#     print("出错了！")
#     print(f"错误是：{e}")
    
# with open("diary.txt","w",encoding="utf-8") as f:
#     f.write("今天学了try except\n")
#     f.write("今天还学了文件读写")
# with open("diary.txt","r",encoding="utf-8") as f:
#     count1 = f.read()
#     print(count1)

# try:
#     num1 = int(input("请输入第一个数字："))
#     num2 = int(input("请输入第二个数字："))
#     print(f"{num1/num2}")
# except Exception as e:
#     print("输入无效，请重试。")

# users = [
#     {"name": "张三", "age": 20, "vip": True},
#     {"name": "李四", "age": 25, "vip": False},
#     {"name": "王五", "age": 22, "vip": True}
# ]
# with open("user.txt","w",encoding="utf-8") as f:
#     for user in users:
#         f.write(users["name"],users["age"],users["vip"])
# with open("user.txt","r",encoding="utf-8") as f:
#     content = f.read()
#     print(f"{content}\n")

#第284行到第294行代码是错误的，改正如下：
# users = [
#     {"name": "张三", "age": 20, "vip": True},
#     {"name": "李四", "age": 25, "vip": False},
#     {"name": "王五", "age": 22, "vip": True}
# ]
# with open("user.txt","w",encoding="utf-8") as f:
#     for user in users:
#         f.write(f"{user['name']} {user['age']} {user['vip']}\n")
# with open("user.txt","r",encoding="utf-8") as f:
#     content = f.read()
#     print(f"{content}\n")

# import json

# users = [
#     {"name": "张三", "age": 20, "vip": True},
#     {"name": "李四", "age": 25, "vip": False},
#     {"name": "王五", "age": 22, "vip": True}
# ]
# with open("user.json","w",encoding="utf-8") as f:
#     json.dump(users,f,ensure_ascii=False,indent=4)
# with open("user.json","r",encoding="utf-8") as f:
#     content = json.load(f)
#     print(f"{content}\n")

# import requests

# request = requests.get("https://api.github.com")
# print(request.status_code)

# import requests

# try:
#     response = requests.get("https://api.github.com/users/torvalds", timeout=5)  # 设置超时时间为5秒
#     data = response.json()
#     print(data["name"])
#     print(data["followers"])
# except requests.exceptions.RequestException as e:   ##requests.exceptions.RequestException是针对网络请求的异常类
#     print(f"请求出错：{e}")

# import json

# my_data = {"prompt":"你好","model":"gpt-4"}
# print(my_data)
# json_string = json.dumps(my_data,ensure_ascii=False)
# print(json_string)
# print(type(json_string))

#类里不应该出现input()，应该在类外部获取输入后传入类的构造函数
# class Student:
#     def __init__(self,name,score):
#         self.name = input("请输入学生姓名：")
#         self.score = int(input("请输入学生成绩："))
#     def is_pass(self):
#         if self.score >= 60:
#             return "及格"
#         else:
#             return "不及格"
# student1 = Student("","")
# print(f"{student1.name}的成绩是{student1.score}，{student1.is_pass()}")
# student2 = Student("","")
# print(f"{student2.name}的成绩是{student2.score}，{student2.is_pass()}")

#改正之后的代码如下：
# class Student:
#     def __init__(self,name,score):
#         self.name = name
#         self.score = score
#     def is_pass(self):
#         if self.score >= 60:
#             return "及格"
#         else:
#             return "不及格"
# name1 = input("请输入学生姓名：")
# score1 = int(input("请输入学生成绩："))
# student1 = Student(name1, score1)
# print(f"{student1.name}的成绩是{student1.score}，{student1.is_pass()}")
# name2 = input("请输入学生姓名：")
# score2 = int(input("请输入学生成绩："))
# student2 = Student(name2, score2)
# print(f"{student2.name}的成绩是{student2.score}，{student2.is_pass()}")

#如下代码是错误的，应该在循环中捕获异常，而不是在循环外部捕获异常
# scores = [85,"90",78,None]
# average = 0
# try:
#     for score in scores:
#         if score is None:
#             raise ValueError("成绩不能为空")
#         elif not isinstance(score,int):
#             raise TypeError("成绩必须是整数")
# except TypeError as e:
#     print(f"类型错误：{e}")
# except ValueError as e:
#     print(f"值错误：{e}")

#改正之后的代码如下：
# scores = [85,"90",78,None]
# total = 0
# valid_score_count = 0
# for score in scores:
#     try:
#         total += float(score)
#         valid_score_count += 1
#     except (ValueError, TypeError):
#         continue
# if valid_score_count > 0:
#     average = total / valid_score_count
#     print(f"平均成绩为：{average}")
# else:
#     print("没有有效的成绩")

#这个属于脚本，而作业是系统
# student_list = []
# total = 0
# average = 0
# class Student:
#     def __init__(self,name,score):
#         self.name = name
#         self.score = score
# while True:
    # try:
    #     name = input("请输入学生姓名：")
    #     score = int(input("请输入学生成绩："))
    # except (ValueError, TypeError):
    #     print("输入无效，请重新输入")
    #     continue
    # student_list.append(Student(name,score))
#     cmd = input("输入q退出：")
#     if cmd == "q":
#         break
# if len(student_list) == 0:
#         print("暂无学生")
# else:
#     for student in student_list:
#         print(f"{student.name}的成绩是{student.score}")
#         total += student.score
#         average = total / len(student_list)
#     print(f"总成绩为：{total}，平均成绩为：{average}")

#根据作业提供的框架，将脚本改为一个简单的系统
# import json

# student_list = []

# class Student:
#     def __init__(self,name,score):
#         self.name = name
#         self.score = score
    
#     def __str__(self): 
#         return f"姓名：{self.name} 成绩：{self.score}"

# try:
#     with open("students.json", "r", encoding="utf-8") as f:
#         data_from_file = json.load(f)
#         student_list = []
#         for item in data_from_file:
#             student_list.append(Student(item["name"], item["score"]))
# except FileNotFoundError:
#     student_list = []

# while True:
#     print("---- 学生成绩管理系统 ----")
#     print("1. 录入学生")
#     print("2. 打印全部学生")
#     print("3. 计算平均分")
#     print("q. 退出系统")
#     choice = input("请选择操作： ")
#     if choice == "1":
#         try:
#             name = input("请输入学生姓名：")
#             score = int(input("请输入学生成绩："))
#         except (ValueError, TypeError):
#             print("输入无效，请重新输入")
#             continue
#         student_list.append(Student(name,score))
#     elif choice == "2":
#         if len(student_list) == 0:
#             print("暂无学生")
#         else:
#             for student in student_list:
#                 print(f"{student.name}的成绩是{student.score}")
#     elif choice == "3":
#         if len(student_list) == 0:
#             print("暂无学生")
#         else:
#             total = 0
#             for student in student_list:
#                 total += student.score
#             average = total / len(student_list)
#             print(f"总成绩为：{total}，平均成绩为：{average}")
#     elif choice == "q":
#         print("退出系统")
        
#         data_to_save = []
#         for student in student_list:
#             data_to_save.append({"name": student.name, "score": student.score})
        
#         with open("students.json", "w", encoding="utf-8") as f:
#             json.dump(data_to_save, f, ensure_ascii=False, indent=4)
#         break
#     else:
#         print("输入错误，请重新选择！")

from student_manager import (
    add_student,
    calculate_average,
    delete_student,
    find_student,
    load_data,
    save_data,
    show_students,
    updata_student,
)

student_list = load_data()

import os

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

def pause():
    input("按回车键返回菜单...")

while True:
    clear_screen()
    print("---- 学生成绩管理系统 ----")
    print("1. 录入学生")
    print("2. 打印全部学生")
    print("3. 计算平均分")
    print("4. 删除学生")
    print("5. 查找学生")
    print("6. 修改成绩")
    print("q. 退出系统")
    choice = input("请选择操作： ")
    if choice == "1":
        add_student(student_list)
    elif choice == "2":
        show_students(student_list)
    elif choice == "3":
        calculate_average(student_list)
    elif choice == "4":
        delete_student(student_list)
    elif choice == "5":
        find_student(student_list)
    elif choice == "6":
        updata_student(student_list)
    elif choice == "q":
        print("退出系统")
        save_data(student_list)
        break
    else:
        print("输入错误，请重新选择！")
    pause()