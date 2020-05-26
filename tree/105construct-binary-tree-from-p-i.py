# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # recursion: O(n), O(n)
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        def build(pos, pleft, pright, ileft, iright):
            if pleft > pright or ileft > iright:
                return None
            root_val = preorder[pleft]
            root = TreeNode(root_val)
            root_index = pos[root_val]
            root.left = build(pos, pleft + 1, root_index + pleft - ileft, ileft, root_index - 1)
            root.right = build(pos, root_index + pleft - ileft + 1, pright, root_index + 1, iright)
            return root

        pleft, pright = 0, len(preorder) - 1
        ileft, iright = 0, len(inorder) - 1

        pos = {}
        for i in range(len(inorder)):
            pos[inorder[i]] = i

        return build(pos, pleft, pright, ileft, iright)

    # slicing (O(n) itself)
    def buildTree1(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if len(inorder) == 0 or len(preorder) == 0:
            return None

        root = TreeNode(preorder[0])
        # better to save hashmap outside the recursion
        # hashmap = {v: i for i, v in enumerate(inorder)}
        # mid = hashmap[preorder[0]]

        mid = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1: mid + 1], inorder[:mid])
        root.right = self.buildTree(preorder[mid + 1:], inorder[mid + 1:])

        return root
