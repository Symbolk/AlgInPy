import numpy as np
import matplotlib.pyplot as plt


# 计算欧几里得距离
def euclidean_distance(a, b):
    return np.sqrt(np.sum((a - b) ** 2))


# K-Means 算法
def kmeans(X, k, max_iters=100):
    # 随机选择初始质心
    centroids = X[np.random.choice(X.shape[0], k, replace=False)]

    for _ in range(max_iters):
        # 分配每个点到最近的质心
        labels = np.array([np.argmin([euclidean_distance(x, centroid) for centroid in centroids]) for x in X])

        # 更新质心
        new_centroids = np.array([X[labels == i].mean(axis=0) for i in range(k)])

        # 检查质心是否变化
        if np.all(centroids == new_centroids):
            break

        centroids = new_centroids

    return centroids, labels


# 示例数据
np.random.seed(0)
X = np.random.rand(100, 2)  # 生成100个二维随机点

# 执行 K-Means
k = 3
centroids, labels = kmeans(X, k)

# 绘制结果
plt.scatter(X[:, 0], X[:, 1], c=labels, cmap='viridis', marker='o')
plt.scatter(centroids[:, 0], centroids[:, 1], c='red', marker='X', s=200, label='Centroids')
plt.title('K-Means Clustering')
plt.legend()
plt.show()
