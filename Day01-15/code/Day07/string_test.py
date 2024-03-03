

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

#对列表进行排序
a = [5,3,4,2,1]
print(sorted(a))

#对元组进行排序
a = (5,4,3,1,2)
print(a)
print(sorted(a))

#字典默认按照key进行排序
a = {4:1,\
 5:2,\
 3:3,\
 2:6,\
 1:8}
print(sorted(a.items()))

#对集合进行排序
a = {1,5,3,2,4}
print(sorted(a))

#对字符串进行排序
a = "51423"
print(sorted(a))

chars=['http://c.biancheng.net',\
 'http://c.biancheng.net/python/',\
 'http://c.biancheng.net/shell/',\
 'http://c.biancheng.net/java/',\
 'http://c.biancheng.net/golang/']
#默认排序
print(sorted(chars))

#自定义按照字符串长度排序
print(sorted(chars,key=lambda x:len(x)))

list1 = ['orange', 'apple', 'zoo', 'internationalization', 'blueberry']
list2 = sorted(list1)
# sorted函数返回列表排序后的拷贝不会修改传入的列表
# 函数的设计就应该像sorted函数一样尽可能不产生副作用
list3 = sorted(list1, reverse=True)
# 通过key关键字参数指定根据字符串长度进行排序而不是默认的字母表顺序
list4 = sorted(list1, key=len)
print(list1)
print(list2)
print(list3)
print(list4)
# 给列表对象发出排序消息直接在列表对象上进行排序
list1.sort(reverse=True)
print(list1)
