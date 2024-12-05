import numpy as np


# 计算欧几里得距离
def euclidean_distance(point1, point2):
    return np.sqrt(np.sum((point1 - point2) ** 2))


# 最近邻搜索函数
def nearest_neighbor(points, target):
    closest_point = None
    min_distance = float('inf')

    for point in points:
        distance = euclidean_distance(point, target)
        if distance < min_distance:
            min_distance = distance
            closest_point = point

    return closest_point, min_distance


# 示例数据
points = np.array([
    [1, 2],
    [3, 4],
    [5, 6],
    [7, 8],
    [2, 1]
])

target = np.array([4, 5])

# 执行最近邻搜索
closest_point, distance = nearest_neighbor(points, target)

print(f"最近的点是: {closest_point}, 距离为: {distance}")
