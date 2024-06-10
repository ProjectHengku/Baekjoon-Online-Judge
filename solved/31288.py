import random


def isPrimeSmall(target):
    # 에라토스테네스의 체
    isPrime = [True] * (target + 1)
    isPrime[0] = isPrime[1] = False
    for i in range(2, int(target ** 0.5) + 1):
        if isPrime[i]:
            for j in range(i * i, target + 1, i):
                isPrime[j] = False

    return isPrime


def isPrimeBig(target):
    k = 27
    # 밀러-라빈 소수 판별법
    if target == 2 or target == 3:
        return True
    if target % 2 == 0 or target < 2:
        return False
    s = 0
    d = target - 1
    while d % 2 == 0:
        s += 1
        d //= 2
    for _ in range(k):
        a = random.randint(2, target - 2)
        x = pow(a, d, target)
        if x == 1 or x == target - 1:
            continue
        for _ in range(s - 1):
            x = pow(x, 2, target)
            if x == 1:
                return False
            if x == target - 1:
                break
        else:
            return False
    return True


def findDivisor(target):
    # 약수 찾기
    div = 2
    success = False
    while div < 10000:
        if target % div == 0:
            success = True
            break
        else:
            div += 1

    if success:
        return div
    else:
        return False


T = int(input())
is_prime = isPrimeSmall(100000)

for _ in range(T):
    N, P = map(int, input().split())
    count = 0
    orig_num = str(P)
    # 될 때 까지 돌린다
    while count < N:
        flag = True
        # 일의 자리부터 수 바꾸면서 다음 자리로 옮김 
        for d in range(N):
            numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
            already_exist = int(orig_num[(N - 1) - d])
            numbers.remove(already_exist)

            # 마지막 자리 수일 경우에는 0이 들어갈 수 없음
            if d == N - 1:
                numbers.remove(0)

            for n in range(9):
                new_num = int(orig_num[:(N - 1) - d] + str(numbers.pop()) + orig_num[N - d :])
                # 소수 판정함
                if P < 100000:
                    if not is_prime[new_num] and findDivisor(new_num):
                        print(new_num, findDivisor(new_num))
                        count += 1
                        if count == N:
                            flag = False
                            break
                else:
                    if not isPrimeBig(new_num) and findDivisor(new_num):
                        print(new_num, findDivisor(new_num))
                        count += 1
                        if count == N:
                            flag = False
                            break
            if not flag:
                break