x = 0
y = 1
for i in range(20):
    x, y = y, x + y
    print(x, end=' ')
