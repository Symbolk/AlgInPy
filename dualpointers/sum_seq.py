def print_res(i, j):
    # print(str(i) + '-' + str(j))
    print(','.join(map(str, range(i, j + 1))))


# O(n^2)

def fun(n):
    for i in range(1, (n + 1) // 2):
        total = i
        for j in range(1, (n + 1) // 2 + 1):
            total += (i + j)
            if total == n:
                print_res(i, i + j)
                break


def fun3(n):
    for i in range(1, (n + 1) // 2):
        total = i
        for j in range(i + 1, (n + 1) // 2 + 1):
            total += j
            if total == n:
                print_res(i, j)
                break


import math


def fun0(n):
    # enum length of the range: k+1
    for k in range(1, (int(math.sqrt(8 * n + 1) - 1) // 2)):
        t = (2 * n - k ** 2 - k)
        if t > 0 and (t / (2 * k + 2)).is_integer():
            print_res(t // (2 * k + 2), t // (2 * k + 2) + k)


# O(n)
def fun1(n):
    if n == 1:
        print('Invalid')
    if n == 2:
        print_res(1, 2)

    i, j = 1, 2
    total = i + j

    while i < (n + 1) // 2:
        if total == n:
            print_res(i, j)
        while total > n:
            total -= i
            i += 1
            if total == n:
                print_res(i, j)
        j += 1
        total += j


def fun2(n):
    i, j = 1, 2
    total = i + j
    while i <= (n + 1) // 2:
        if total == n:
            print_res(i, j)
            total -= i
            i += 1
            j += 1
            total += j
        elif total > n:
            total -= i
            i += 1
        else:
            j += 1
            total += j


fun(15)
fun0(15)
fun1(15)
fun2(15)
