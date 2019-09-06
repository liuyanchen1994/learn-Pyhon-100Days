"""
猜数字游戏
计算机出一个1~100之间的随机数由人来猜
计算机根据人猜的数字分别给出提示大一点/小一点/猜对了
"""
import random

numguess = random.randint(1, 100)

while True:
    num = int(input('请输入数字：'))
    if num > numguess:
        print('猜的数字太大')
    elif num < numguess:
        print('猜的数字太小')
    else:
        print('猜对了')
        break
