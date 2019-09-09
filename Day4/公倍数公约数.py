"""
输入两个正整数计算最大公约数和最小公倍数
（a,b) * [a,b]=a*b
"""
a = int(input("请输入第一个正整数："))
b = int(input("请输入第二个正整数："))
if a > b:
    a, b = b, a
for i in range(a, 0, -1):
    if a % i == 0 and b % i == 0:
        print('最大公约数是：%d' % i)
        print('最小公倍数是：%d' % (a * b // i))
        break
