import random
from collections import deque


def bubble_sort(arr):
    length = len(arr)
    for i in range(length - 1):
        for j in range(length - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


def selection_sort(arr):
    length = len(arr)
    for i in range(length - 1):
        min_index = i
        for j in range(i + 1, length):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr


def insertion_sort(arr):
    length = len(arr)
    for i in range(1, length):
        pre_index = i - 1
        current = arr[i]
        while pre_index >= 0 and arr[pre_index] > current:
            arr[pre_index + 1] = arr[pre_index]
            pre_index -= 1
        arr[pre_index + 1] = current
    return arr


# iteratively merge_sort sub-array (python slicing makes it tidier)
def merge_sort(arr):
    length = len(arr)
    # for sorting, 0/1 return instantly
    if length < 2:
        return arr
    mid = length >> 1  # length/2
    left = arr[:mid]
    right = arr[mid:]
    return merge(merge_sort(left), merge_sort(right))


def merge(left, right):
    res = []
    while len(left) > 0 and len(right) > 0:
        # while left and right:
        # < --> unstable
        res.append(left.pop(0) if left[0] < right[0] else right.pop(0))
    res = res + left + right
    return res


# use index to divide and conquer (regular way)
def merge_sort2(arr, l, r):
    if l < r:
        mid = l + ((r - l) >> 1)
        merge_sort2(arr, l, mid)
        merge_sort2(arr, mid + 1, r)
        merge2(arr, l, mid, r)
    return arr


def merge2(arr, l, mid, r):
    temp = [0] * (r - l + 1)
    i = l
    j = mid + 1
    k = 0
    while i <= mid and j <= r:
        if arr[i] < arr[j]:
            temp[k] = arr[i]
            i += 1
        else:
            temp[k] = arr[j]
            j += 1
        k += 1
    while i <= mid:
        temp[k] = arr[i]
        i += 1
        k += 1
    while j <= r:
        temp[k] = arr[j]
        j += 1
        k += 1
    for i in range(len(temp)):
        arr[l + i] = temp[i]


# directly merge into the original arr
def merge_sort_in_place(arr, l, r):
    if l < r:
        mid = l + ((r - l) >> 1)
        merge_sort_in_place(arr, l, mid)
        merge_sort_in_place(arr, mid + 1, r)
        merge_in_place(arr, l, mid, r)
    return arr


def merge_in_place(arr, l, mid, r):
    left = arr[l:mid + 1]
    right = arr[mid + 1:r + 1]
    k = l
    while left and right:
        arr[k] = left.pop(0) if left[0] < right[0] else right.pop(0)
        k += 1
    tail = left if left else right
    for n in tail:
        arr[k] = n
        k += 1


# iteration
def quick_sort(arr, l, r):
    if l >= r:
        return arr
    # pivot_index = partition1(arr, l, r)
    pivot_index = partition2(arr, l, r)
    quick_sort(arr, l, pivot_index - 1)
    quick_sort(arr, pivot_index + 1, r)
    return arr


# single loop
def partition1(arr, l, r):
    # first or random as the pivot
    pivot = arr[l]
    index = l
    for i in range(l + 1, r + 1):
        if arr[i] < pivot:
            index += 1
            arr[index], arr[i] = arr[i], arr[index]
    arr[l], arr[index] = arr[index], arr[l]
    return index


# double loop
def partition2(arr, l, r):
    pivot = arr[l]
    index = l

    while l != r:
        # scan from right to left, find the last element <= pivot
        while l < r and arr[r] > pivot:
            r -= 1
        # scan from left to right, find the first element > pivot
        while l < r and arr[l] <= pivot:
            l += 1
        if l < r:
            arr[l], arr[r] = arr[r], arr[l]

        # arr[index] = arr[l]
        # arr[l] = pivot
        arr[index], arr[l] = arr[l], pivot
    return l


def heap_sort(arr):
    # index start from 1
    heap = deque(arr)
    heap.appendleft(0)

    length = len(heap) - 1
    # the last node with children
    last_non_leaf = length >> 1
    for i in range(last_non_leaf):
        heapify(heap, last_non_leaf - i, length)

    for i in range(length - 1):
        heap[1], heap[length - i] = heap[length - i], heap[1]
        heapify(heap, 1, length - i - 1)

    return [heap[i] for i in range(1, len(heap))]


def heapify(heap, start, end):
    tmp = heap[start]  # parent
    i = start  # left child index
    j = i * 2  # right child index

    while j <= end:
        if j < end and heap[j] < heap[j + 1]:
            j += 1  # record the index of the larger child
        if tmp < heap[j]:  # if the parent is smaller than child
            heap[i] = heap[j]  # switch the child with the parent
            # adjust the next level
            i = j
            j = i * 2
        else:
            break
    heap[i] = tmp


if __name__ == "__main__":
    arr = [random.randint(0, 100) for _ in range(10)]
    # print(bubble_sort(arr))
    # print(selection_sort(arr))
    # print(insertion_sort(arr))
    # print(merge_sort(arr))
    # print(merge_sort_in_place(arr, 0, len(arr) - 1))
    # print(merge_sort2(arr, 0, len(arr) - 1))
    print(quick_sort(arr, 0, len(arr) - 1))
    # print(quick_sort2(arr, 0, len(arr) - 1))
    # print(heap_sort(arr))
