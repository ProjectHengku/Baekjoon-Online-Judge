import sys

input = sys.stdin.readline


def miller_rabin(target, a, s, d):
    x = pow(a, d, target)
    if x == 1 or x == target - 1:
        return True
    else:
        for _ in range(s):
            x = pow(x, 2, target)
            if x == target - 1:
                return True

        return False


def isPrime(target):
    if target < 2 or not target & 1:
        return False

    if target == 2:
        return True

    s = 0
    d = target - 1
    while d % 2 == 0:
        s += 1
        d //= 2

    for a in (2, 3, 5, 7, 11):
        if not miller_rabin(target, a, s, d):
            return False

    return True


N = int(input())

invalid = 0
for _ in range(N):
    area = int(input())

    if area < 4:
        invalid += 1
    else:
        if isPrime(2 * area + 1):
            invalid += 1

print(invalid)
