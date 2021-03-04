from tkinter import Tk,Label,Button

class MyFirstGUI:
    def __init__(self,master):
        self.master=master
        master.title("A simple GUI")

        # 生成标签,将标签添加到主窗口
        self.label=Label(master,text="This is our first GUI!")
        self.label.pack()

        # 生成Greet按钮,将按钮添加到root主窗口
        self.greet_button=Button(master,text="Greet",command=self.greet)
        self.greet_button.pack()

        # 生成close按钮,将按钮添加到master主窗口
        self.close_button=Button(master,text="Close",command=master.quit)
        self.close_button.pack()

    def greet(self):
        print("Greetings!")

# 生成主窗口
root=Tk()
my_gui=MyFirstGUI(root)
# 进入消息循环(必须组件)
root.mainloop()