'''
    1.理解has a 一个类使用了另外一种自定义的类型
        student使用computer book
    2.类型的概念：
        系统类型：str、int、float、list....
        自定义类型：自定义的类,都可以将其当成一种类型
                s=Student()
                s是Student类型的对象
'''


class Book:
    def __init__(self, bname, author):
        self.bname = bname
        self.author = author

    def __str__(self):
        return self.bname + '-------' + self.author


class Computer:
    def __init__(self, brand, size, type):
        self.brand = brand
        self.size = size
        self.type = type

    def online(self):
        print('正在上网中。。。。。。')

    def __str__(self):
        return self.brand + '====' + self.type + '++++' + self.size


class Student:  # has a
    def __init__(self, name, computer, book):
        self.name = name
        self.computer = computer
        self.books = []
        self.books.append(book)

    def borrow_book(self, book):
        for book1 in self.books:
            if book.bname == book1.bname:
                print('已经借过了这本书')
                break
            else:
                # 将参数book添加到列表中
                self.books.append(book)
                print('添加成功！')

    def show_book(self):
        for book in self.books:
            print(book.bname)

    def __str__(self):
        return self.name + '-------' + str(self.computer) + '--------' + str(self.books)


# 创建对象
comp = Computer('MAC_2020', '22', 'IM17')

book = Book('神龙', '小芬')

stu = Student('UZI', comp, book)
print(stu)

# 看接了哪些书
stu.show_book()

book1 = Book('幻城', '小郭')

stu.borrow_book(book1)

print('=============================')
stu.show_book()
