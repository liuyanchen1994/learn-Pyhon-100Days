"""
求10000以内的完美数
"""

for i in range(2, 10001):
    sum = 0
    for j in range(1, i):
        if i % j == 0:
            sum += j
    if i == sum:
        print(i)

# import math
#
# for num in range(1, 10000):
#     result = 0
#     for factor in range(1, int(math.sqrt(num)) + 1):
#         if num % factor == 0:
#             result += factor
#             if 1 < factor != num // factor:
#                 result += num // factor
#     if result == num:
#         print(num)
