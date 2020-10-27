# 计算汇率
def money_dollar(rmb_str_value):
    # 常量汇率
    USD_VS_RMB = 6.28
    # 汇率计算
    usd = rmb_str_value * USD_VS_RMB
    return usd


# 美元输入，将字符串转换为数字
rmb_str_value = int(input('请输入要转换的美元金额：'))
# 输出结果 转换后人民币金额
print('转换后人民币金额是：', money_dollar(rmb_str_value))
