"""
输入一个正整数判断它是不是素数
"""
x = int(input('输入一个正整数：'))
is_prime = True
if x != 1:
    for i in range(2, x):
        if x % i == 0:
            is_prime = False
        break
else:
    is_prime = False

print(is_prime)
