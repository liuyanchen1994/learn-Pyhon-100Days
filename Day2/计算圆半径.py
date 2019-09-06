"""
输入圆半径计算圆半径和周长
S=πr^2
C=2πr
"""

import math

radius=int(input('请输入半径='))
s=math.pi*radius*radius
c=2*math.pi*radius

print('圆的面积是：%d' % s)
print('圆的周长是：%d' % c)