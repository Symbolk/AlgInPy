from typing import List


class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        last_pos = [-1] * 26
        # dic = {c:i for i, s in enumerate(S)}
        for i, c in enumerate(S):
            last_pos[ord(c) - ord('a')] = i  # just override is ok

        res = []
        start = end = 0
        for i, c in enumerate(S):
            # find the last last pos of letters in S[start:end+1]
            end = max(end, last_pos[ord(c) - ord('a')])
            if i == end:
                res.append(end - start + 1)
                start = end + 1
        return res


s = Solution()
print(s.partitionLabels("ababcbacadefegdehijhklij"))
