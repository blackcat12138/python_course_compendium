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
        pass

    def __str__(self):
        return self.name + '-------' + str(self.computer) + '--------' + str(self.books)


# 创建对象
comp = Computer('MAC_2020', '22', 'IM17')

book = Book('神龙', '小芬')

stu = Student('UZI', comp, book)

print(stu)
