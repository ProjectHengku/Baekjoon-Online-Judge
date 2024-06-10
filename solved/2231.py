N = int(input())

# M이 아무리 작아봤자 N - 9 * len(str(N)) 보다 작을 수 없다.
M = N - len(str(N)) * 9
if M < 0:
    M = 1

M2 = 0

# M 의 각 자리 수의 합을 구하는 함수
def sum_digit(num):
    sum = 0
    while num > 0:
        sum += num % 10
        num = num // 10
    return sum

# M2와 N을 비교해서 될 때 까지 반복
while True:
    M2 = sum_digit(M) + M

    if M2 == N:
        break
    elif M > N:
        M = 0
        break
    else:
        M += 1

print(M)