'''
    公路(Road)：
        属性:公路名称,公路长度
    车(Car)：
        属性：车名,时速
        方法：1.求车名在那条公路上以多少的时速行驶多长,
                get_time(self,road)
              2.初始化车属性信息__init__方法
              3.打印对象显示车的属性信息

'''
from random import random


# 定义Road类
class Road:
    def __init__(self, name, len):
        self.name = name
        self.len = len


# 定义Car类
class Car:
    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed

    def get_time(self, road):  # road=r 两者同时指向同一个地址空间
        ran_time = random.randint(1, 10)
        msg = '{}品牌的车在{}上,以{}速度行驶{}小时'.format(self.brand, road.name, self.speed, ran_time)
        print(msg)

    def __str__(self):
        return '{}品牌的,速度：{}'.format(self.brand, self.speed)


# 创建实例化对象
r = Road('京广高速', 12000)

aodi = Car('奥迪', 120)

print(aodi)

aodi.get_time(r)
