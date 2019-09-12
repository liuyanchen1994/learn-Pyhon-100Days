"""
鸡翁一值钱五，鸡母一值钱三，鸡雏三值钱一
"""
for x in range(20):
    for y in range(33):
        if x * 5 + 3 * y + (100 - x - y) / 3 == 100:
            print('公鸡：%d只，母鸡：%d，小鸡：%d' % (x, y, 100 - x - y))
