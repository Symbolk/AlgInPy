"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = []):
        self.val = val
        self.neighbors = neighbors
"""


class Solution:
    def __init__(self):
        # key: node, value: clone node
        self.visited = {}

    # DFS: search and clone O(n), O(n)
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None
        if node in self.visited:
            return self.visited[node]

        clone = Node(node.val, [])
        self.visited[node] = clone

        if node.neighbors:
            clone.neighbors = [self.cloneGraph(n) for n in node.neighbors]

        return clone

    # DFS
    def cloneGraph0(self, node: 'Node') -> 'Node':
        visited = {}

        def dfs(n):
            if not n:
                return n
            if n in visited:
                return visited[n]
            clone = Node(n.val, [])
            visited[n] = clone
            if n.neighbors:
                for nei in n.neighbors:
                    clone.neighbors.append(dfs(nei))
            return clone

        return dfs(node)

    # BFS: O(n), O(n)
    def cloneGraph1(self, node: 'Node') -> 'Node':
        if not node:
            return node
        q = collections.deque()
        visited = {}

        q.append(node)
        visited[node] = Node(node.val, [])

        while q:
            n = q.popleft()
            for nei in n.neighbors:
                if nei not in visited:
                    visited[nei] = Node(nei.val, [])
                    q.append(nei)
                visited[n].neighbors.append(visited[nei])
        return visited[node]
