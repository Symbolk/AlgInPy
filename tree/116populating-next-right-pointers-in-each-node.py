"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""


class Solution:
    # bfs: O(n), O(n)
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root
        cur = collections.deque([root])
        while cur:
            size = len(cur)
            for i in range(size):
                node = cur.popleft()
                if i < size - 1:  # notice here
                    node.next = cur[0]
                if node.left:
                    cur.append(node.left)
                if node.right:
                    cur.append(node.right)
        return root

    # recursion
    def connect1(self, root: 'Node') -> 'Node':
        if not root:
            return root

        def fun(cur_level):
            next_level = []
            for node in cur_level:
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)

            if len(next_level) > 1:
                for i in range(len(next_level) - 1):
                    next_level[i].next = next_level[i + 1]
            if next_level:
                fun(next_level)

        fun([root])
        return root
