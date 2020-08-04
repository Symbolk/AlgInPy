# 定义树状数组
class BIT(object):
    def __init__(self, size):
        self.size = size
        self.tree = [0] * (size + 1)

    def __lowbit(self, index):
        return index & (-index)

    def update(self, index, delta):
        while index <= self.size:
            self.tree[index] += delta
            index += self.__lowbit(index)

    def query(self, index):
        res = 0
        while index > 0:
            res += self.tree[index]
            index -= self.__lowbit(index)
        return res


from collections import deque


class Solution:
    def minInteger(self, num: str, k: int) -> str:
        num = [int(x) for x in num]  # 输入转换成数字列表
        num_rec = [deque() for _ in range(10)]  # 记录每个数字(0,1,2,...9)的出现位置，保存在deque中, 便于删除
        for i, x in enumerate(num):  # 填写num_rec
            num_rec[x].append(i)
        rst = []  # 保存最终的输出
        bit = BIT(len(num))  # 树状数字，bit.query(i) 表示在num[:i]中被移动到rst的元素数量

        while (k > 0):  # 如果k>0，即还有操作次数，则继续移动
            for digit in range(10):  # 找下一个要移动的数
                idx = -1  # 保存下一个要移动的数的坐标
                if num_rec[digit]:  # 如果 num_rec[digit] 不为空
                    k_to_use = num_rec[digit][0] - bit.query(num_rec[digit][0])
                    if k_to_use <= k:  # 且num_rec[digit]最少要移动的次数小于等于k
                        idx = num_rec[digit].popleft()  # 则下一个要移动的坐标为idx，并且将这个idx出num_rec[digit]中删除
                        break  # 停止遍历，因为digit是递增，举例来说，如果digit为0能满足要求，则一定先移动0
            if idx == -1: break  # 找不到要移动的数，说明num_rec已经空了, 所有的元素都被操作过了, 结束循环
            rst.append(digit)
            k -= k_to_use  # 减去这次需要移动的次数
            num[idx] = -1  # num[idx]现在被用过了，标记为-1，在后面返回结果要用到
            bit.update(idx + 1, 1)  # num[idx]被用过了，在bit中也要更新一下
            # print(bit.nums, rst, k) # debug
        for x in num:  # 最后再遍历一遍，把num中没用到的数字加在后面
            if x != -1: rst.append(x)
        return "".join([str(c) for c in rst])
