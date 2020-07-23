class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        parent = {}

        def find(x):
            # ! setdefault() actually do get(), only set the default value if key not exists
            parent.setdefault(x, x)
            # find root to shorten path
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            parent[find(x)] = find(y)

        for e in equations:
            if e[1] == '=':
                x = ord(e[0]) - ord('a')
                y = ord(e[3]) - ord('a')
                union(x, y)
        for e in equations:
            if e[1] == '!':
                x = ord(e[0]) - ord('a')
                y = ord(e[3]) - ord('a')
                if find(x) == find(y):
                    return False
        return True

    def equationsPossible1(self, equations: List[str]) -> bool:
        uf = UnionFind(26)
        for e in equations:
            if e[1] == '=':
                x = ord(e[0]) - ord('a')
                y = ord(e[3]) - ord('a')
                uf.union(x, y)

        for e in equations:
            if e[1] == '!':
                x = ord(e[0]) - ord('a')
                y = ord(e[3]) - ord('a')
                if uf.is_connected(x, y):
                    return False
        return True


# use a class & array for union-find
class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))

    # 隔代压缩
    def find1(self, x):
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

    # 完全压缩
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        self.parent[self.find(x)] = self.find(y)

    def is_connected(self, x, y):
        return self.find(x) == self.find(y)
