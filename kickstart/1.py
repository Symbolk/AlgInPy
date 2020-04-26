T = int(input().strip())

for t in range(T):
    N = int(input())
    data = [int(s) for s in input().split(" ")]
    if len(data) <= 1:
        print("Case #{}: {}".format(str(t+1), "0"))
        continue
    ans = 0
    for i in range(1, len(data)):
        if i + 1 < len(data):
            if data[i] > data[i + 1] and data[i] > data[i-1]:
                ans += 1
    print("Case #{}: {}".format(str(t+1), str(ans)))

# str_in = input()
#
# for case in range(int(str_in)):
#     _ = input()
#     str_in = input()
#     lst = [int(x) for x in str_in.split()]
#
#     res = 0
#
#     for i in range(1, len(lst) - 1):
#         if lst[i] > lst[i - 1] and lst[i] > lst[i + 1]:
#             res += 1
#
#     print("Case #{}: {}".format(case + 1, res))

