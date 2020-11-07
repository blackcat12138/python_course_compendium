# 定义类
class Student:
    # 类属性
    name = 'uzi'
    age = 3


# 使用类,创建对象
mlxg = Student()
print(mlxg.age)


class Phone:
    brand = "小米"
    price = 40000
    type = 'mate 400'

    def call(self):
        print('正在打电话....')


p1 = Phone()
print(p1.brand)
p1.call()

