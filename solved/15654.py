def perm(depth, left, numbers):
    numlst = list(numbers)
    numlst.sort()
    for i in numlst:
        if depth == M:
            print((left + " " + str(i)).strip())
        else:
            perm(depth + 1, left + " " + str(i), numbers - {i})


N, M = map(int, input().split())
numbers = set(map(int, input().split()))

perm(1, "", numbers)
