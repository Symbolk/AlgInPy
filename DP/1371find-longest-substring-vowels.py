class Solution(object):
    def findTheLongestSubstring(self, s):
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