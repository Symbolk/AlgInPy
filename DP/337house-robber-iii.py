# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import defaultdict


class Solution:
    # memorized dfs: O(n), O(n)
    def rob(self, root: TreeNode) -> int:
        f = defaultdict(int)  # rob
        g = defaultdict(int)  # not rob

        def dfs(node):
            if not node:
                return
            dfs(node.left)
            dfs(node.right)
            f[node] = node.val + g[node.left] + g[node.right]
            g[node] = max(f[node.left], g[node.left]) + max(f[node.right], g[node.right])

        dfs(root)
        return max(f[root], g[root])

    # tree dp: O(n), O(n)
    def rob1(self, root: TreeNode) -> int:
        def dfs(v):
            if not v:
                return (0, 0)
            l = dfs(v.left)
            r = dfs(v.right)
            # 0 means not rob, 1 means rob
            rob = v.val + l[0] + r[0]
            notrob = max(l[0], l[1]) + max(r[0], r[1])
            return (notrob, rob)

        return max(dfs(root))
