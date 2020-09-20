import random
from typing import List


# [a, b]
# print(random.randint(0, 9))

def findK(nums, k):
    N = len(nums)
    l, r = 0, N - 1
    i = partition(nums, l, r)
    # if i == N - k: found
    # if i > N - k: N-k in left of i
    # if i < N - k: N-k in right of i
    while i != N - k:
        if i > N - k:
            r = i - 1
        else:
            l = i + 1
        i = partition(nums, l, r)
    return nums[i]


def partition(nums, l, r):
    # select the rightmost as pivot
    pivot = nums[r]

    i = l
    for j in range(l, r):
        if nums[j] < pivot:
            nums[j], nums[i] = nums[i], nums[j]
            i += 1

    nums[i], nums[r] = nums[r], nums[i]
    return i


def findK2(nums, k):
    return qsort(nums, k, 0, len(nums) - 1)


def qsort(nums, k, l, r):
    pivot = nums[l]
    i, j = l, r
    # [bigger] pivot [smaller]
    while i < j:
        # find the right first > pivot
        while i < j and nums[j] <= pivot:
            j -= 1
        nums[i] = nums[j]
        # find the left first < pivot
        while i < j and nums[i] >= pivot:
            i += 1
        nums[j] = nums[i]
    nums[j] = pivot

    if j == k - 1:
        return pivot
    elif j > k - 1:  # in left
        return qsort(nums, k, l, j - 1)
    else:
        return qsort(nums, k, j + 1, r)


arr = [2, 3, 7, 1, -4, 5, 11, 34, 2, 54, 343, 3]
for i in range(1, len(arr) + 1):
    print(findK(arr, i))

for i in range(1, len(arr) + 1):
    print(findK2(arr, i))
# nums = list(map(int,input()[1:-1].split(',')))
# print(nums)
