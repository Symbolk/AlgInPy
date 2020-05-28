class Solution(object):
    # prefix sum, binary, bitwise: O(n), O(1)
    def findTheLongestSubstring(self, s):
        res = 0
        state = 0
        # binary: 00001, 00010, 00100, 01000, 10000
        vowel = {'a': 1, 'e': 2, 'i': 4, 'o': 8, 'u': 16}
        # state: index
        map = {0: -1}
        for i in range(len(s)):
            c = s[i]
            if c in vowel:  # if vowel.get(c)
                state ^= vowel[c]
                if state not in map:
                    map[state] = i
            length = i - map[state]
            res = max(res, length)
        return res

    def findTheLongestSubstring1(self, s):
        res = 0
        # odd(1) or even(0) for each vowel, all possible state is 32 (2^5)
        state = 0
        N = len(s)
        # 1 << 5 = 2^5 = 32
        pos = [-1] * (1 << 5)
        pos[0] = 0
        for i in range(N):
            # no switch in Python
            if s[i] == 'a':
                state ^= (1 << 0)
            elif s[i] == 'e':
                state ^= (1 << 1)
            elif s[i] == 'i':
                state ^= (1 << 2)
            elif s[i] == 'o':
                state ^= (1 << 3)
            elif s[i] == 'u':
                state ^= (1 << 4)
            if pos[state] == -1:
                # state first time appears
                pos[state] = i + 1
            else:
                # state has appeared before, pre-pre == 00000!
                res = max(res, i + 1 - pos[state])
        return res

    # simplifed
    def findTheLongestSubstring2(self, s):
        res = 0
        state = 0
        pos = [0] + [-1] * 31
        for i, c in enumerate(s):
            if c in 'aeiou':
                state ^= (1 << 'aeiou'.index(c))
            if pos[state] == -1:
                pos[state] = i + 1
            else:
                res = max(res, i + 1 - pos[state])
        return res

    def findTheLongestSubstring3(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 0
        state = [-1] * (1 << 5)
        cur, state[0] = 0, 0
        d = dict(zip('aeiou', range(5)))
        for idx, val in enumerate(s):
            tmp = -1
            if val in d:
                tmp = d[val]
            if tmp != -1:
                cur ^= 1 << tmp
            if state[cur] == -1:
                state[cur] = idx + 1
            else:
                res = max(res, idx + 1 - state[cur])
        return res


sol = Solution()
print(sol.findTheLongestSubstring1("eleetminicoworoep"))
