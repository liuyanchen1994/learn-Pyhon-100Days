"""
英制单位与公制单位互换
1英寸=2.54厘米
"""
a = float(input('请输入长度：'))
unit = input('请输入单位：')
if unit == '英寸':
    print('%d英寸等于%d厘米' % (a, a * 2.54))
elif unit == '厘米':
    print('%d厘米等于%d英寸' % (a, a / 2.54))
else:
    print('请输入正确的单位')
