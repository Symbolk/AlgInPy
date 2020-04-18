import math

n, m = map(int, input().strip().split())
cost = list(map(int, input().strip().split()))
k = int(input().strip())
cost.sort()

for _ in range(k):
    ans = 0
    t = int(input().strip())
    stocks = cost[:t]
    stocks.sort(reverse=True)
    if t <= m:
        for i in range(t):
            ans += stocks[i]
    else:
        i = 0
        for d in range(math.ceil(t / m)):
            end = i + m if i + m <= t else t
            for j in range(i, end):
                ans += (d + 1) * stocks[j]
            i += m
    print(ans)
