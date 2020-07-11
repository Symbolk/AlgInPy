from typing import List


class Solution:
    # brutal force: O(sum(w_i^2))
    # preserve all words that are not suffix of other words
    def minimumLengthEncoding(self, words: List[str]) -> int:
        wordSet = set(words)
        for w in words:
            for i in range(1, len(w)):
                # wordSet.discard(w[1:w])
                suffix = w[i:]
                if suffix in wordSet:
                    wordSet.remove(suffix)
        res = 0
        for w in wordSet:
            res += len(w) + 1

        return res

    # reversed + trie: O(sum(w_i)) (pythonic)
    def minimumLengthEncoding1(self, words: List[str]) -> int:
        words = list(set(words))  # remove duplicates
        # Trie is a nested dictionary with nodes created
        # when fetched entries are missing
        import collections
        Trie = lambda: collections.defaultdict(Trie)
        trie = Trie()

        from functools import reduce
        nodes = [reduce(dict.__getitem__, w[::-1], trie) for w in words]
        return sum(len(w) + 1 for i, w in enumerate(words) if len(nodes[i]) == 0)

    # implement trie by recursion
    def minimumLengthEncoding2(self, words: List[str]) -> int:
        # def trie
        class Node:
            def __init__(self, n):
                self.n = n
                self.children = {}

        def build(t, w):
            if not w:
                return
            if w[-1] not in t.children:
                t.children[w[-1]] = Node(t.n + 1)
            build(t.children[w[-1]], w[:-1])

        # build trie
        root = Node(0)
        for w in words:
            build(root, w)
        ans = [0]

        def visit(t):
            if len(t.children) == 0:  # leaf
                if t.n > 0:
                    ans[0] += t.n + 1
            for c in t.children.values():
                visit(c)

        visit(root)
        return ans[0]

    # sort by reversed words
    def minimumLengthEncoding3(self, words: List[str]) -> int:
        N = len(words)
        # define comparator to sort according to suffix
        words.sort(key=lambda w: w[::-1])

        res = 0
        for i in range(N):
            if i + 1 < N and words[i + 1].endswith(words[i]):
                pass
            else:
                res += len(words[i]) + 1
        return res

    # reversed words and sort
    def minimumLengthEncoding4(self, words: List[str]) -> int:
        N = len(words)
        # reverse words and sort
        words = sorted([w[::-1] for w in words])

        res = 0
        for i in range(N):
            if i + 1 < N and words[i + 1].startswith(words[i]):
                pass
            else:
                res += len(words[i]) + 1
        return res


sol = Solution()
print(sol.minimumLengthEncoding(["time", "me", "bell"]))
print(sol.minimumLengthEncoding2(["time", "me", "bell"]))
