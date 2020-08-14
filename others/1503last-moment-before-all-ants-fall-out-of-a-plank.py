class Solution:
    # when meet&turn, it makes no difference! O(n), O(1)
    def getLastMoment(self, n: int, left: List[int], right: List[int]) -> int:
        time = 0
        # left: the position of left-ward ant when t=0
        if left:
            time = max(time, max(left))
        if right:
            time = max(time, n - min(right))
        return time
