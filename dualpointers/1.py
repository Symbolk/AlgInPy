# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A, K):
    # write your code in Python 3.6
    L = len(A)
    if L == 0:
        return A
    if K == L:
        return A
    if K < L:
        return A[L-K:L] + A[0:L-K]
    if K > L:
        kk = K % L
        return A[L-kk:L] +  A[0:L-kk]


print(solution([3,8,9,7,6], 5))
print(solution([], 99))