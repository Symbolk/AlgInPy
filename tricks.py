if __name__ == '__main__':
    li = [1, 2, 3, 4, 5]  # 列表本身不包含数据1,2,3,4,5，而是包含变量：li[0] li[1] li[2] li[3] li[4]
    first = li[0]  # 拷贝列表，也不会有数据对象的复制，而是创建新的变量引用
    del li[0]
    # print(li)  # 输出[2, 3, 4, 5]
    # print(first)  # 输出 1

    for i, j in zip(range(5), range(4)):
        print(i)
        print(j)

    i, j = 0, 5
    while i < j:
        print(i)
        i += 1
        print("<")
        print(j)
        j -= 1

    for (i, j) in [(x, x) for x in range(3)]:
        print(str(i) + "==" + str(j))
