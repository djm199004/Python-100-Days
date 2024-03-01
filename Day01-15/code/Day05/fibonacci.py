"""
输出斐波那契数列的前20个数
1 1 2 3 5 8 13 21 ...

Version: 0.1
Author: 骆昊
Date: 2018-03-02
"""

a = 0
b = 1
for _ in range(20):
    a, b = b, a + b
    print(a, end=' ')

'''
Version: 0.1
Author: 董家明
Date: 2024-03-01
'''
print('/n')
a = 0
b = 1
sum = 0
for _ in range(20):
    sum = a + b
    a = b
    b = sum
    print(a, end=' ')
