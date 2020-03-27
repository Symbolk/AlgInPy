# Greatest Common Divider O(log(max(a,b)))
def gcd(a, b):
    return b if a % b == 0 else gcd(b, a % b)


def gcd2(a, b):
    return a if b == 0 else gcd(b, a % b)

# Least Common Multiple
def lcm(a, b):
    return int(a / gcd(a, b) * b)


raw = input()
n, m = raw.split(' ')
n, m = int(n), int(m)
print(gcd(n, m))
print(gcd2(n, m))
print(lcm(n, m))
