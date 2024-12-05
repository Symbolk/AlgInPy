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
        self.nums[i] = val

    def sumRange(self, i: int, j: int) -> int:
        if j + 1 > len(self.nums):
            j = len(self.nums) - 1
        res = 0
        for k in range(1, j-i+1):
            if i + k + 1 <= j:


T = int(input().strip())
for t in range(T):
    N, Q = map(int, input().strip().split())
    arr = list(map(int, input().strip().split()))
    ftarray = NumArray(arr)
    res = 0
    for n in range(Q):
        op = list(input().strip().split())
        if op[0] == 'U':
            ftarray.update(int(op[1]) - 1, int(op[2]))
        elif op[0] == 'Q':
            qres = ftarray.sumRange(int(op[1]) - 1, int(op[2]) - 1)
            res += qres
            print(qres)
    print('Case #{}: {}'.format(str(t + 1), str(res)))
