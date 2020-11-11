class Cellphone:
    def __init__(self):
        print('智能手机的默认语言为英文')

    def cellphone(self, defaultLanguage):
        print('将智能手机默认语言设置为' + defaultLanguage)


Cellphone().cellphone('中文')
