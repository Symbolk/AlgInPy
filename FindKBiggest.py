import random
from typing import List


# [a, b]
# print(random.randint(0, 9))

def findK(arr, k):
    n = len(arr)
    l, r = 0, n - 1
    i = partition(arr, l, r)
    while i != n - k:
        if i > n - k:
            r = i - 1
            i = partition(arr, l, i - 1)
        else:
            l = i + 1
            i = partition(arr, i + 1, r)
    return arr[i]


def partition(data_list, begin, end):
    partition_key = data_list[end]

    index = begin
    for i in range(begin, end):
        if data_list[i] < partition_key:
            data_list[i], data_list[index] = data_list[index], data_list[i]
            index += 1

    data_list[index], data_list[end] = data_list[end], data_list[index]
    return index


arr = [2, 3, 7, 1, -4, 5, 11, 34, 2, 54, 343, 3]
for i in range(1, len(arr) + 1):
    print(findK(arr, i))
# nums = list(map(int,input()[1:-1].split(',')))
# print(nums)
