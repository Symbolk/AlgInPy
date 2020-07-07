# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # double iteration
    def count(self, root, sum):
        if not root:
            return 0
        # the sum of the sub problems
        sum -= root.val
        cnt = 0
        if sum == 0:
            cnt += 1
        return cnt + self.count(root.left, sum) + self.count(root.right, sum)

    def pathSum(self, root: TreeNode, sum: int) -> int:
        if not root:
            return 0
        # start from: root, left child, right child
        return self.count(root, sum) + self.pathSum(root.left, sum) + self.pathSum(root.right, sum)

    # presum
    def pathSum1(self, root: TreeNode, sum: int) -> int:
        def dfs(node, presum):
            if not node:
                return 0
            presum = [s + node.val for s in presum] + [node.val]
            return presum.count(sum) + dfs(node.left, presum) + dfs(node.right, presum)

        return dfs(root, [])

    # presum count
    def pathSum2(self, root: TreeNode, sum: int) -> int:
        presum_cnt = {0: 1}

        def pretree(node, presum_cnt, cur_sum):
            if not node:
                return 0
            res = 0
            cur_sum += node.val
            # find the times of the cur_sum - target
            res += presum_cnt.get(cur_sum - sum, 0)
            presum_cnt[cur_sum] = presum_cnt.get(cur_sum, 0) + 1
            res += pretree(node.left, presum_cnt, cur_sum)
            res += pretree(node.right, presum_cnt, cur_sum)
            # restore state
            presum_cnt[cur_sum] -= 1
            return res

        return pretree(root, presum_cnt, 0)
