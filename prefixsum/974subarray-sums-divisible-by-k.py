class Solution:
    # 规律：连续子数组---前缀和；统计出现次数---散列表
    # Python: floored division, so mod of negative (to -inf) is different
    # C/CPP, Java, JS, PHP: truncated division (to 0 when negative)

    # naive presum: O(n^2), O(n), TLE
    def subarraysDivByK(self, A: List[int], K: int) -> int:
        N = len(A)
        res = 0
        presum = [0] * (N + 1)
        for i in range(N):
            presum[i + 1] = presum[i] + A[i]
        for i in range(N):
            for j in range(i + 1, N):
                if (presum[j] - presum[i]) % K == 0:
                    res += 1
        return res

    # TLE: O(n^2), O(n)
    def subarraysDivByK1(self, A: List[int], K: int) -> int:
        from collections import defaultdict
        res = 0
        cur_sum = 0
        # presum: cnt
        precnt = defaultdict(int)  # factory method to provide the default value, int default 0
        # precnt = dict()
        # presum = 0 appears once
        precnt[0] = 1
        for n in A:
            cur_sum += n
            for k in precnt:
                if (cur_sum - k) % K == 0:
                    res += precnt[k]
            precnt[cur_sum] += 1
        return res

    # O(n), O(min(n,k)
    def subarraysDivByK2(self, A: List[int], K: int) -> int:
        from collections import defaultdict
        res = 0
        premod = 0
        precnt = defaultdict(int)
        precnt[0] = 1
        for n in A:
            premod = (premod + n) % K
            res += precnt[premod]  # if not exist, + 0
            precnt[premod] += 1
        return res

    def subarraysDivByK22(self, A: List[int], K: int) -> int:
        res = 0
        cursum = 0
        precnt = {0: 1}
        for a in A:
            cursum += a
            modulus = cursum % K
            same = precnt.get(modulus, 0)
            res += same
            precnt[modulus] = same + 1
        return res
