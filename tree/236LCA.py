class Solution:
    def lowestCommonAncestor(self, root, p, q):
        if not root or root == p or root == q:
            return root
        l = self.lowestCommonAncestor(root.left, p, q)
        r = self.lowestCommonAncestor(root.right, p, q)
        if l and r:
            return root
        elif l:
            return l
        elif r:
            return r
        return None

    def lowestCommonAncestor2(self, root, p, q):
        # node : node.parent
        parent = {root: None}

        def dfs(node):
            if node:
                if node.left:
                    parent[node.left] = node
                if node.right:
                    parent[node.right] = node
                dfs(node.left)
                dfs(node.right)

        dfs(root)
        l1, l2 = p, q
        while l1 != l2:
            # get or default
            l1 = parent.get(l1, q)
            l2 = parent.get(l2, p)
        return l1
