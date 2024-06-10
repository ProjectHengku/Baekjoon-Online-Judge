import sys

sys.setrecursionlimit(10**7)


def preorder(start_in, end_in, start_post, end_post):
    if (start_in > end_in) or (start_post > end_post):
        return 0

    root = postorder[end_post]
    root_pos_in = inorder_position[root]
    print(root, end=" ")

    size_left = root_pos_in - start_in
    size_right = end_in - root_pos_in

    # apart left and right sub tree
    preorder(start_in, start_in + size_left - 1, start_post, start_post + size_left - 1)
    preorder(end_in - size_right + 1, end_in, end_post - size_right, end_post - 1)


n = int(input())
inorder = list(map(int, input().split()))
postorder = list(map(int, input().split()))

# index inorder positions
inorder_position = [0] * (n + 1)
for i in range(n):
    inorder_position[inorder[i]] = i

preorder(0, n - 1, 0, n - 1)
