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
        else:
            l = i + 1
        i = partition(arr, l, r)
    return arr[i]


def partition(nums, left, right):
    pivot = nums[right]

    index = left
    for i in range(left, right):
        if nums[i] < pivot:
            nums[i], nums[index] = nums[index], nums[i]
            index += 1

    nums[index], nums[right] = nums[right], nums[index]
    return index


arr = [2, 3, 7, 1, -4, 5, 11, 34, 2, 54, 343, 3]
for i in range(1, len(arr) + 1):
    print(findK(arr, i))
# nums = list(map(int,input()[1:-1].split(',')))
# print(nums)
