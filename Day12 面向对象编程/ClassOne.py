'''
    类定义和使用
'''


class Student:
    # self参数：接收消息的学生对象
    def study(self, course_name):
        print(f'学生正在学习{course_name}.')

    def play(self):
        print(f'学生正在玩游戏.')


# 创建stu1学生对象
stu1 = Student()
# 通过"类.方法"调用方法;第一个参数：接收消息的对象;第二个参数：学生的课程名称
Student.study(stu1, "数学")
# 通过"对象.方法"调用方法
stu1.study("语文")

stu2 = Student()
Student.play(stu2)
stu2.play()
