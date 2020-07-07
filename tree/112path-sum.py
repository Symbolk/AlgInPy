# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque


class Solution:
    # BFS: path sum from root to leaf: O(n), O(n)
    def hasPathSum1(self, root: TreeNode, sum: int) -> bool:
        if not root:
            return False
        q = deque()
        q.append((root, root.val))
        while q:
            node, cur_sum = q.popleft()
            if not node.left and not node.right:
                if cur_sum == sum:
                    return True
                else:
                    continue
            if node.left:
                q.append((node.left, cur_sum + node.left.val))
            if node.right:
                q.append((node.right, cur_sum + node.right.val))
        return False

    # DFS or iteration: O(n), O(logn~n)
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if not root:
            return False
        if not root.left and not root.right:
            return sum == root.val
        return self.hasPathSum(root.left, sum - root.left.val) or self.hasPathSum(root.right, sum - root.right.val)
