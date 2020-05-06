class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        # the min cost to travel to the day
        # add extra 0 to keep in line with index
        dp = [0 for _ in range(days[-1] + 1)]
        days_idx = 0
        for i in range(1, len(dp)):
            # if not the wanted day, cost same
            if i != days[days_idx]:
                dp[i] = dp[i - 1]
            else:
                # if is the wanted day, select a min cost from 3 tickets
                dp[i] = min(dp[max(0, i - 1)] + costs[0],
                            dp[max(0, i - 7)] + costs[1],
                            dp[max(0, i - 30)] + costs[2])
                days_idx += 1
        # return the min cost to travel to the last day
        return dp[-1]
