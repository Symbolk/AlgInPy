str_in = input()


# simulate the moving
def solve(strr):
    w = 0
    h = 0

    # use stack to store the repeat times
    depth = [1]
    # current step length
    curr = 1

    for i, s in enumerate(strr):
        if s == "(":
            # append the repeat times (number [0, 9])
            depth.append(int(strr[i - 1]))
            # increase the step length by times
            curr = curr * depth[-1]
        if s == ")":
            # done with the last repeat subseq(...)
            last = depth.pop()
            # restore the step length (think as the multiplication formula)
            curr = curr // last

        if s == "W":
            w -= curr
        if s == "E":
            w += curr

        if s == "N":
            h -= curr
        if s == "S":
            h += curr

    # move in loop: %
    return w % (10 ** 9), h % (10 ** 9)


for case in range(int(str_in)):
    strr = input()
    w, h = solve(strr)

    # start from [1, 1]
    print("Case #{}: {} {}".format(case + 1, w + 1, h + 1))

# T = int(input().strip())
# def parse(seq):
#     depth = 0
#     res = []
#     while seq:
#         s = seq.pop()
#         if s == ')':
#             depth += 1
#         elif s == '(':
#             depth -= 1
#
#
#
# print(parse(list('2(3(NW)2(W2(EE)W))')))

# for t in range(T):
#     line = input().strip()
#     seq = parse(list(line))
#     print(seq)
#
# 4
# SSSEEE
# N
# N3(S)
# N2(E)
# N
# 2(3(NW)
# 2(W2(EE)
# W))
#
#
# Case  # 1: 4 4
# Case  # 2: 1 1000000000
# Case  # 3: 3 1
# Case  # 4: 3 999999995
