def preorder(root):
    global ans_preorder

    ans_preorder += root
    if tree[root][0]:
        preorder(tree[root][0])
    if tree[root][1]:
        preorder(tree[root][1])


def inorder(root):
    global ans_inorder

    if tree[root][0]:
        inorder(tree[root][0])
    ans_inorder += root
    if tree[root][1]:
        inorder(tree[root][1])


def postorder(root):
    global ans_postorder

    if tree[root][0]:
        postorder(tree[root][0])
    if tree[root][1]:
        postorder(tree[root][1])
    ans_postorder += root


N = int(input())
tree = {}
for _ in range(N):
    node, childL, childR = input().split()
    tree[node] = [0, 0]
    if childL != ".":
        tree[node][0] = childL
    if childR != ".":
        tree[node][1] = childR

ans_preorder = ""
ans_inorder = ""
ans_postorder = ""

preorder("A")
inorder("A")
postorder("A")

print(ans_preorder)
print(ans_inorder)
print(ans_postorder)
