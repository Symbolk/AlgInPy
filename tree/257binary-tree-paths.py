# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # recursion: O(N), O(N) (stack space in the worst case)
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        paths = []

        def find(node, path):
            if node:
                path += str(node.val)
                # path.append(str(node.val))
                if not node.left and not node.right:
                    paths.append(path)
                else:
                    path += '->'
                    find(node.left, path)
                    # if path is list (mutable), must restore state here
                    find(node.right, path)

        find(root, '')
        # res = []
        # for p in paths:
        #     res.append('->'.join(p))
        return paths

    # DFS: O(N), O(N)
    def binaryTreePaths1(self, root: TreeNode) -> List[str]:
        if not root:
            return []
        paths = []
        # use the stack to keep the current path
        stack = [(root, str(root.val))]
        while stack:
            node, path = stack.pop()
            if not node.left and not node.right:
                paths.append(path)
            if node.left:
                stack.append((node.left, path + '->' + str(node.left.val)))
            if node.right:
                stack.append((node.right, path + '->' + str(node.right.val)))
        return paths
