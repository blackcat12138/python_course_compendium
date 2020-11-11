class Credit:
    def __init__(self, cardNum, password="123456"):
        if password == "123456":
            print("信用卡" + cardNum + "的默认密码为" + password)
        else:
            print("重置信用卡" + cardNum + "的密码为" + password)


Credit("421087199403247312")
Credit("421087199403247312", "1345628")
