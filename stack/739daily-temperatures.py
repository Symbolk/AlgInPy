class Solution:
    # monotonicity stack: O(n), O(n)
    # when to use? if need to find the first bigger/smaller num/pos
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        N = len(T)
        res = [0] * N
        stack = []
        for i in range(N):
            t = T[i]
            while stack and t > T[stack[-1]]:
                # stack keeps the index, not temperature
                prev = stack.pop()
                res[prev] = i - prev
            stack.append(i)
        return res

    # reversed brutal
    def dailyTemperatures1(self, T: List[int]) -> List[int]:
        N = len(T)
        res = [0] * N
        for i in range(N - 2, -1, -1):
            for j in range(i + 1, N, res[j]):
                if T[i] < T[j]:
                    res[i] = j - i
                    break
                elif res[j] == 0:
                    res[i] = 0
                    break
        return res
