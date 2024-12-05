def max_product_split(N):
    if N == 2:
        return 1  # 1 * 1
    if N == 3:
        return 2  # 1 * 2

    product = 1

    while N > 4:
        product *= 3
        N -= 3

    product *= N  # 处理剩下的部分
    return product


# 示例
N = 10
result = max_product_split(N)
print(f"N = {N}, 最大乘积 = {result}")
