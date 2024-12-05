def quicksort(arr, low, high):
    if low < high:
        # 获取分区索引
        pi = partition(arr, low, high)

        # 递归排序分区
        quicksort(arr, low, pi - 1)  # 排序基准左侧
        quicksort(arr, pi + 1, high)  # 排序基准右侧

def partition(arr, low, high):
    # 选择最后一个元素作为基准
    pivot = arr[high]
    i = low - 1  # 小于基准的元素的索引

    for j in range(low, high):
        # 如果当前元素小于或等于基准
        if arr[j] <= pivot:
            i += 1  # 增加小于基准的元素索引
            arr[i], arr[j] = arr[j], arr[i]  # 交换元素

    # 将基准元素放到正确的位置
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1  # 返回基准元素的索引

# 示例用法
if __name__ == "__main__":
    arr = [10, 7, 8, 9, 1, 5]
    print("原数组:", arr)
    quicksort(arr, 0, len(arr) - 1)
    print("排序后数组:", arr)
