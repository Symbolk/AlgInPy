from typing import List


class FenwickTree:
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


class NumArray:
    def __init__(self, nums: List[int]):
        self.ft = FenwickTree(len(nums))
        self.nums = nums
        for i in range(len(nums)):
            self.ft.update(i + 1, nums[i])

    def update(self, i: int, val: int) -> None:
        self.ft.update(i + 1, val - self.nums[i])

    def sumRange(self, i: int, j: int) -> int:
        return self.ft.query(j + 1) - self.ft.query(i)


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(i,val)
# param_2 = obj.sumRange(i,j)

arr = NumArray([1, 3, 5])
print(arr.sumRange(0, 2))
print(arr.update(1, 2))
print(arr.sumRange(0, 2))
