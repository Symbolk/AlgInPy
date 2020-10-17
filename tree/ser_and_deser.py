class Solution:
    def __init__(self):
        self.seq = []

    def serialize(self, node):
        self.seq.append(node.val)
        if node.left:
            self.seq.append(self.serialize(node.left))
        if node.right:
            self.seq.append(self.serialize(node.right))

    def deserialize(self, seq):
        if not seq:
            return
        s = seq[0]
        seq.pop(0)
        node = TreeNode(s)
        node.left = self.deserialize(seq)
        node.right = self.deserialize(seq)

        return node
