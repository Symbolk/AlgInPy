T = int(input().strip())

for t in range(T):
    N, K = map(int, input().strip().split())
    arr = list(map(int, input().strip().split()))
    i, j = 0, K - 1
    res = 0
    while j < N:
        if arr[i] == K and arr[j] == 1:
            found = True
            for k in range(i, j):
                if arr[k] - arr[k + 1] != 1:
                    found = False
                    break
            if found:
                res += 1
        i += 1
        j += 1
    print('Case #{}: {}'.format(str(t + 1), str(res)))
