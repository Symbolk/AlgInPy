def fun(N, L):
    # N, L = map(int, input().strip().split())
    for i in range(L, 101):
        if (2 * N + i - i * i) % (2 * i) == 0:
            start = (2 * N + i - i * i) // (2 * i)
            if start < 0:
                print('No')
                exit()
            ans = [str(j) for j in range(start, start + i)]
            print(' '.join(ans))
            exit()
    print('No')


fun(18, 2)
