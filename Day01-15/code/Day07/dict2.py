"""
字典的常用操作

Version: 0.1
Author: 骆昊
Date: 2018-03-06
"""


def main():
    stu = {'name': '骆昊', 'age': 38, 'gender': True}
    print(stu)
    print(stu.keys())
    print(stu.values())
    print(stu.items())
    for elem in stu.items():
        print(elem)
        print(elem[0], elem[1])
    if 'age' in stu:
        stu['age'] = 20
    print(stu)
    stu.setdefault('score', 60)
    print(stu)
    stu.setdefault('score', 100)
    print(stu)
    stu['score'] = 100
    print(stu)

    list_ = [1, 2, 3]
    print(list_, f'has a length of {len(list_)}.')
    # [1,2,3] has a length of 3.
    print(list_, f'has a length of {{len(list_)}}.')
    # [1,2,3] has a length of {len(list_)}.
    print(list_, f'has a length of {{{len(list_)}}}.')
    print(list_, 'has a length of len(list_).')

if __name__ == '__main__':
    main()
