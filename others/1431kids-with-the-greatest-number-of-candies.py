class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxCandies = max(candies)
        # list comprehension
        res = [candy + extraCandies >= maxCandies for candy in candies]
        return res