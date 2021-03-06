from typing import List


class Solution(object):
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordSet = set(wordList)
        if endWord not in wordSet:
            return 0

        res = 1
        n = len(beginWord)
        current = set()
        current.add(beginWord)

        while current:
            next_level = set()
            if endWord in current:
                return res
            for cur in current:
                if cur in wordSet:
                    wordSet.remove(cur)
                for i in range(n):
                    for ch in range(97, 123):
                        tmp = cur[:i] + chr(ch) + cur[i + 1:]
                        if tmp in wordSet:
                            next_level.add(tmp)
            res += 1
            current = next_level
        return 0

    def ladderLength2(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordSet = set(wordList)
        if endWord not in wordSet:
            return 0

        res = 1
        wordDict = {}
        for w in wordSet:
            for i in range(len(w)):
                new_w = w[:i] + "_" + w[i + 1:]
                if new_w in wordDict:
                    wordDict[new_w].append(w)
                else:
                    wordDict[new_w] = [w]

        current = [beginWord]
        next_level = []
        while current:
            for w in current:
                if w == endWord:
                    return res
                for i in range(len(w)):
                    new_w = w[:i] + "_" + w[i + 1:]
                    if new_w in wordDict:
                        for t in wordDict[new_w]:
                            if t not in next_level:
                                next_level.append(t)
                        del wordDict[new_w]
            res += 1
            current = next_level
            next_level = []
        return 0

    # bidirectional BFS
    def ladderLength3(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordList = set(wordList)
        if endWord not in wordList:
            return 0
        front = {beginWord}
        back = {endWord}
        res = 1
        L = len(beginWord)

        import string
        while front:
            res += 1
            next = set()
            for word in front:
                for i in range(L):
                    for c in string.ascii_lowercase:
                        if c != word[i]:
                            new_word = word[:i] + c + word[i + 1:]
                            if new_word in back:
                                return res
                            if new_word in wordList:
                                next.add(new_word)
                                wordList.remove(new_word)
            front = next
            if len(back) < len(front):
                front, back = back, front
        return 0


solution = Solution()
print(solution.ladderLength2("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))
print(solution.ladderLength3("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))
