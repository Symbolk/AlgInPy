# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # O(n), O(n)
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        res = []
        cur_level = [root]
        while cur_level:
            next_level = []
            tmp = []
            for node in cur_level:
                tmp.append(node.val)
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            res.append(tmp)
            cur_level = next_level
        return res[::-1]

    def levelOrderBottom1(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        res = []

        # nodes of the current level
        q = collections.deque([root])
        while q:
            # vals of the current level
            level = []
            num = len(q)
            for _ in range(num):
                node = q.popleft()
                level.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            res.append(level)
        return res[::-1]
