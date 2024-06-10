import sys

sys.setrecursionlimit(1000001)


def postorder(tree):
    root = tree[0]

    left = []
    right = []

    if len(tree) > 1:
        for idx, value in enumerate(tree[1:]):
            if value > root:
                left = tree[1 : idx + 1]
                right = tree[idx + 1 :]
                break
        else:
            left = tree[1:]

    if left:
        postorder(left)
    if right:
        postorder(right)
    print(root)


input = sys.stdin.readline

get = []
while True:
    try:
        get.append(int(input()))
    except:
        break

postorder(get)
