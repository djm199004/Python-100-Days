

s1 = 'hello, world!'
s2 = "hello, world!"
# 以三个双引号或单引号开头的字符串可以折行
s3 = """
hello, 
world!
"""
print(s1, s2, s3, end='')

s1 = '\'hello, world!\''
s2 = '\n\\hello, world!\\\n'
print(s1, s2, end='')

s1 = '\141\142\143\x61\x62\x63'
s2 = '\u9a86\u660a'
print(s1, s2)

s1 = r'\'hello, world!\''
s2 = r'\n\\hello, world!\\\n'
print(s1, s2, end='')

s1 = 'hello ' * 3
print(s1) # hello hello hello
s2 = 'world'
s1 += s2
print(s1) # hello hello hello world
print('ll' in s1) # True
print('good' in s1) # False
print('ho' in s1) # False

str1 = 'abc def'
# 通过内置函数len计算字符串的长度
print(len(str1)) # 7
# 获得字符串首字母大写的拷贝
print(str1.capitalize()) # Abc def
# 获得字符串每个单词首字母大写的拷贝
print(str1.title()) # Abc Def
# 将字符串以指定的宽度居中并在两侧填充指定的字符
print(str1.center(11, '*'))
# 将字符串以指定的宽度靠右放置左侧填充指定的字符
print(str1.rjust(10, '*'))

a, b = 5, 10
print('{0} * {1} = {2}'.format(a, b, a * b))

list1 = [1, 3, 5, 7, 100]
print(list1)
for index, elem in enumerate(list1):
    print(index, elem)
