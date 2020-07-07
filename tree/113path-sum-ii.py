# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from functools import reduce


class Solution:
    # BFS (with stack or deque): O(n), O(n)
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        if not root:
            return []
        stack = [(root, [root.val])]
        res = []
        while stack:
            node, path = stack.pop()
            if not node.left and not node.right:
                cur = reduce(lambda x, y: x + y, path)
                if cur == sum:
                    res.append(path)
            if node.right:
                stack.append((node.right, path + [node.right.val]))
            if node.left:
                stack.append((node.left, path + [node.left.val]))
        return res

    # DFS: O(n), O(n)
    def pathSum1(self, root: TreeNode, sum: int) -> List[List[int]]:
        if not root:
            return []
        res = []

        def dfs(node, path, s):
            if not node:
                return
            if not node.left and not node.right:
                if s == node.val:
                    # tmp + [root.val] generate and return a new list
                    path += [node.val]
                    res.append(path)
            dfs(node.left, path + [node.val], s - node.val)
            dfs(node.right, path + [node.val], s - node.val)

        dfs(root, [], sum)
        return res

    # backtrack
    def pathSum2(self, root: TreeNode, sum: int) -> List[List[int]]:
        if not root:
            return []
        res = []

        def backtrack(node: TreeNode, path: List[int], cur_sum: int):
            if not node:
                return
            path.append(node.val)
            cur_sum += node.val
            if not node.left and not node.right:
                if cur_sum == sum:
                    # !must create a new list here!
                    res.append(list(path))
                # revert state to backtrack!
                path.pop()
                return
            if node.left:
                backtrack(node.left, path, cur_sum)
            if node.right:
                backtrack(node.right, path, cur_sum)
            # backtrack here!
            path.pop()

        backtrack(root, [], 0)
        return res
