from scipy.stats import binom

# binomial distribution
str_in = input()


def solve(w, h, l, u, r, d):
    # 0,0 start
    # w,h destination
    # l ... d
    # . ... .
    # r ... u

    res = 0
    # 6,4,1,3,3,4
    if u - 2 >= 0 and w > r:
        # cumulative density function
        # binom.cdf(1, 4, 0.5) # 1 = u-2 = 3-2, 4 = r+u-2 = 3+3-2
        res += binom.cdf(u - 2, r + u - 2, 0.5)
    if l - 2 >= 0 and h > d:
        res += binom.cdf(l - 2, d + l - 2, 0.5)

    return res


# kickstart likes misleading descriptions

# it says 'W columns (numbered 1 to W from left to right) and H rows (numbered 1 to H from top to bottom)'
# actually, it means w rows and h columns in normal sense
# it says start from (1,1), but that does not affect the final result, which is only a probability
for case in range(int(str_in)):
    strr = input()
    w, h, l, u, r, d = [int(x) for x in strr.split()]
    prob = solve(w, h, l, u, r, d)

    print("Case #{}: {}".format(case + 1, prob))


# Another
from math import log2
logs = [0] * 200001
# logs[i] = log base 2 of (i!)
for i in range(2, 200001):
    logs[i] = log2(i) + logs[i-1]

T = int(input())

def at_least_k_flips(n, k):
    # find the probability that out of n coin flips, at least k are heads
    result = 0
    for i in range(k, n+1):
        result += pow(2.0, logs[n] - logs[i] - logs[n-i] - n)
    return result

for test in range(T):
    [w, h, l, u, r, d] = list(map(int, input().split(" ")))
    prob_below = at_least_k_flips(l+d-2, d) if h > d else 0
    prob_above = at_least_k_flips(r+u-2, r) if w > r else 0
    #print(prob_below)
    #print(prob_above)
    total_prob = prob_below + prob_above

    print("Case #{}: {}".format(test+1, total_prob))
