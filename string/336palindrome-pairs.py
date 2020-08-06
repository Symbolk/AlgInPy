from typing import List


class Solution:
    # brutal force: O(n^2*L), O(1)
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        def isPalindrome(s):
            l, r = 0, len(s) - 1
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True

        res = []
        N = len(words)
        for i in range(N):
            for j in range(i + 1, N):
                if isPalindrome(words[i] + words[j]):
                    res.append([i, j])
                if isPalindrome((words[j] + words[i])):
                    res.append([j, i])
        return res

    # use hash table: O(n*L^2), O(n*L)
    def palindromePairs1(self, words: List[str]) -> List[List[int]]:
        def isPalindrome(s):
            l, r = 0, len(s) - 1
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True

        N = len(words)
        res = []
        rev = dict()
        for i in range(N):
            rev[words[i][::-1]] = i

        for i in range(N):
            cur = words[i]
            # allow '' + 'aaa'
            if len(cur) > 0 and isPalindrome(cur) and '' in rev:
                res.append([rev[''], i])
            # j to split the cur word
            for j in range(len(cur)):
                left = cur[:j]
                right = cur[j:]
                # if part is palindrome, another part can be reversed to another word
                # then they can be combined to form a bigger palindrome!
                if isPalindrome(left) and right in rev:
                    if rev.get(right) != i:
                        res.append([rev[right], i])
                if isPalindrome(right) and left in rev:
                    if rev.get(left) != i:
                        res.append([i, rev[left]])
        return res


s = Solution()
print(s.palindromePairs(["abcd", "dcba", "lls", "s", "sssll"]))
print(s.palindromePairs1(["abcd", "dcba", "lls", "s", "sssll"]))
