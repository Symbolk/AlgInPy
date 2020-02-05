if __name__ == '__main__':
    attributes = ['name', 'dob', 'gender']
    values = [['jason', '2000-01-01', 'male'], ['mike', '1999-01-01', 'male'], ['nancy', '2001-02-01', 'female']]
    l = []
    for v in values:
        d = {}
        for i in range(0, len(attributes)):
            d[attributes[i]] = v[i]
        l.append(d)
    print(l)
    # zip()接受一系列可迭代的对象作为参数，将其中元素打包成为一个个tuple并返回tuple组成的list
    # 返回list长度为iterable长度，若不等则返回最短长度
    l2 = [dict(zip(attributes, v)) for v in values]
    print(l == l2)
