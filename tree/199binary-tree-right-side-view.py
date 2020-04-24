# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # classic level order traversal
    # get the last (right most) val in each level
    # key: only keeps nodes in the current level in queue, drill down and move on!
    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        res = []
        cur_level = [root]
        while cur_level:
            next_level = []
            res.append(cur_level[-1].val)
            for node in cur_level:
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            cur_level = next_level
        return res

    # DFS aways go right: O(n), O(n)
    # stack: first in, last out, so the first popped is the right most!
    def rightSideView1(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        # depth:right-most-value
        tmp = dict()
        max_depth = -1

        # use tuple to record level
        stack = [(root, 0)]
        while stack:
            node, depth = stack.pop()
            if node:
                max_depth = max(max_depth, depth)
                # only set if not exist
                tmp.setdefault(depth, node.val)
                stack.append((node.left, depth + 1))
                stack.append((node.right, depth + 1))

        return [tmp[depth] for depth in range(max_depth + 1)]

    # BFS: O(n), O(n)
    def rightSideView2(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        from collections import deque
        tmp = dict()
        max_depth = -1

        # use a list to init deque
        q = deque([(root, 0)])
        while q:
            node, depth = q.popleft()
            if node:
                max_depth = max(depth, max_depth)
                # cover the value to keep the last (right most)
                tmp[depth] = node.val
                q.append((node.left, depth + 1))
                q.append((node.right, depth + 1))
        return [tmp[depth] for depth in range(max_depth + 1)]
