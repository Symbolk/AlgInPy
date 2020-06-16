# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    # DFS
    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        res = []

        def serialize(root):
            if root is None:
                res.append('null')
            else:
                res.append(str(root.val))
                serialize(root.left)
                serialize(root.right)

        serialize(root)
        return ','.join(res)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None
        data = data.split(',')

        def deserialize(index):
            if data[index] == 'null':
                return index, None
            else:
                node = TreeNode(int(data[index]))
                l, left = deserialize(index + 1)
                node.left = left
                r, right = deserialize(l + 1)
                node.right = right
                return r, node

        return deserialize(0)[1]

    # BFS
    def serialize1(self, root):
        if not root:
            return ''
        from collections import deque
        q = deque([root])
        res = []
        while q:
            node = q.popleft()
            if node:
                res.append(str(node.val))
                q.extend([node.left, node.right])
            else:
                res.append('null')
        return ','.join(res)

    def deserialize1(self, data):
        if not data:
            return None
        nodes = [(TreeNode(int(v)) if v != 'null' else None) for v in data.split(',')]
        i, j = 0, 1
        while j < len(nodes):
            if nodes[i] is not None:
                nodes[i].left = nodes[j]
                j += 1
                nodes[i].right = nodes[j]
                j += 1
            i += 1
        return nodes[0]

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
