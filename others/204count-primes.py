class Solution:
    # O(sqrt(n))
    def countPrimes(self, n: int) -> int:
        def is_prime(num):
            j = 2
            while j * j <= num:
                if num % j == 0:
                    return False
                j += 1
            return True

        cnt = 0
        for i in range(2, n):
            if is_prime(i):
                cnt += 1

        return cnt

    # O(nloglogn), O(n)
    def countPrimes1(self, n: int) -> int:
        if n < 2:
            return 0

        mark = [1] * n
        cnt = 0

        for i in range(2, n):
            if mark[i]:
                cnt += 1
                # mark composite numbers
                for j in range(i * i, n, i):
                    mark[j] = 0

        return cnt
