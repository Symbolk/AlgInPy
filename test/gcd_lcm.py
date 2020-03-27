# Greatest Common Divider O(log(max(a,b)))
def gcd(a, b):
    return b if a % b == 0 else gcd(b, a % b)


def gcd2(a, b):
    return a if b == 0 else gcd(b, a % b)


# Least Common Multiple
def lcm(a, b):
    return int(a / gcd(a, b) * b)


# input two ints
n, m = map(int, input().split())
print(gcd(n, m), end=", ")
print(gcd2(n, m), end=',')
print(lcm(n, m))
