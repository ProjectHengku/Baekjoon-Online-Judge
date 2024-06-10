def K_repeat(word):
    n = len(word)
    for i in range(1, n // 2 + 1):
        for j in range(n - i):
            count = 0
            unit = word[j : j + i]
            for pos in range(j, n, i):
                tar = word[pos : pos + i]
                if tar == unit:
                    count += 1
                    if count >= K:
                        return True
                else:
                    count = 0
                    break
    return False


def find(length, word):
    if K_repeat(word):
        return 1

    if length == N:
        print(word)
        exit()
        return word

    for letter in range(A):
        find(length + 1, word + chr(a + letter))

    return -1


K, N, A = map(int, input().split())

a = ord("A")

answer = find(0, "")

print(answer)
