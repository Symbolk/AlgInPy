# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # iteration with index range: O(n), O(logn) (stack depth)
    def sortedArrayToBST0(self, nums: List[int]) -> TreeNode:
        def fun(l, r):
            if l > r:
                return None
            m = (l + r) // 2
            root = TreeNode(nums[m])
            root.left = fun(l, m - 1)
            root.right = fun(m + 1, r)
            return root

        return fun(0, len(nums) - 1)

    # iteration with slicing: O(n), O(n^2)
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if not nums:
            return None
        N = len(nums)
        # middle index
        m = (N - 1) // 2
        root = TreeNode(nums[m])
        root.left = self.sortedArrayToBST(nums[:m])
        root.right = self.sortedArrayToBST(nums[m + 1:])
        return root
