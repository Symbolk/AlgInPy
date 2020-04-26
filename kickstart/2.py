# https://codingcompetitions.withgoogle.com/kickstart/round/000000000019ffc8/00000000002d83bf
# Mine
# T = int(input().strip())
#
# for t in range(T):
#     N, D = map(int, input().strip().split())
#     data = list(map(int, input().strip().split()))
#     i, j = (D // data[0]) * data[0], (D // data[-1]) * data[-1]
#     res = 0
#     while 0 <= i <= j:
#         find = [0] * N
#         for k in range(i, j+1):
#             for n in range(N):
#                 if k % data[n] == 0:
#                     find[n] += 1
#         ok = True
#         for f in find:
#             if f == 0:
#                 ok = False
#                 break
#
#         if ok:
#             res = i
#             break
#
#         i -= data[0]
#         j -= data[-1]
#
#     if res:
#         print("Case #{}: {}".format(str(t + 1), str(res)))
#     else:
#         print("Case #{}: {}".format(str(t + 1), '0'))


# Correct: binary search
# str_in = input()
#
#
# def possible(d, lst, start):
#     for x in lst:
#         start = start + (-start) % x
#     if start > d:
#         return False
#     return True
#
#
# def solve(d, lst):
#     upper = 2 ** 41
#     lower = 0
#
#     for _ in range(42):
#         middle = (upper + lower) // 2
#         if not possible(d, lst, middle):
#             upper = middle
#         else:
#             lower = middle
#
#     return middle
#
#
# for case in range(int(str_in)):
#     strr = input()
#     n, d = [int(x) for x in strr.split()]
#     strr = input()
#     lst = [int(x) for x in strr.split()]
#
#     res = solve(d, lst)
#
#     print("Case #{}: {}".format(case + 1, res))

# Another
T = int(input())
for t in range(T):
    N, D = map(int, input().strip().split())
    data = list(map(int, input().strip().split()))
    latest = D
    for x in data[::-1]:
        # find the closest integer that %x = 0
        latest = (latest // x) * x
    print('Case #{}: {}'.format(t + 1, latest))
