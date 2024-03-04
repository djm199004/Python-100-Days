"""
定义和使用字典

Version: 0.1
Author: 骆昊
Date: 2018-03-06
"""


def main():
    scores = {'骆昊': 95, '白元芳': 78, '狄仁杰': 82}
    print(scores['骆昊'])
    print(scores['狄仁杰'])
    print(scores)
    for elem in scores:
        print('%s\t--->\t%d' % (elem, scores[elem]))
    scores['白元芳'] = 65
    scores['诸葛王朗'] = 71
    scores.update(冷面=67, 方启鹤=85)
    print(scores)
    if '武则天' in scores:
        print(scores['武则天'])
    print(scores.get('武则天'))
    print(scores.get('武则天', 60))
    print(scores)
    print(scores.popitem())
    print(scores.popitem())
    print(scores.pop('骆昊', 100))
    print(scores)
    for key in scores:
        print(f'{key}: {scores[key]}')
    scores.clear()
    print(scores)


    # 创建字典的构造器语法
    items1 = dict(one=1, two=2, three=3, four=4)
    # 通过zip函数将两个序列压成字典
    items2 = dict(zip(['a', 'b', 'c'], '123'))
    # 创建字典的推导式语法
    items3 = {num: num ** 2 for num in range(1, 10)}
    print(items1, items2, items3)


if __name__ == '__main__':
    main()
