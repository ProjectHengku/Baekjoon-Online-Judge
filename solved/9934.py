def make_tree(arr, level):
    n = len(arr)
    mid = n // 2
    tree[level].append(arr[mid])

    if n == 1:
        return 1

    make_tree(arr[:mid], level + 1)
    make_tree(arr[mid + 1 :], level + 1)


K = int(input())
bldg = list(map(int, input().split()))

tree = [[] for _ in range(K)]

make_tree(bldg, 0)

for level in tree:
    print(*level)
