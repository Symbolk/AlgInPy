class Solution:
    # recursion: O(n), O(n)
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return None
        if root == p or root == q:
            return root
        l = self.lowestCommonAncestor(root.left, p, q)
        r = self.lowestCommonAncestor(root.right, p, q)
        if l and r:
            return root
        return l if l else r

    # dfs:
    def lowestCommonAncestor1(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        parent = {root: None}

        def dfs(node):
            if node:
                if node.left:
                    parent[node.left] = node
                    dfs(node.left)
                if node.right:
                    parent[node.right] = node
                    dfs(node.right)

        # build a map to cache the parent
        dfs(root)
        l1, l2 = p, q
        while l1 != l2:
            # .get(k, default): if k not exist, return default; if exist, return value
            # .setdefault(k, default): if k not exist, return and set k=default; if exist, return value
            l1 = parent.get(l1, q)
            l2 = parent.get(l2, p)
        return l1
