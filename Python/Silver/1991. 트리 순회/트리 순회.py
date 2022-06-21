def preorder(v):
    if v == '.':
        return
    print(v, end="")
    preorder(tree[v][0])
    preorder(tree[v][1])


# 중위 순회
def inorder(v):
    if v == '.':
        return
    inorder(tree[v][0])
    print(v, end="")
    inorder(tree[v][1])


# 후위 순회
def postorder(v):
    if v == '.':
        return
    postorder(tree[v][0])
    postorder(tree[v][1])
    print(v, end="")

N = int(input())
tree = {}

for i in range(N):
    root, left, right = map(str, input().split())
    tree[root] = left, right

preorder('A')
print()
inorder('A')
print()
postorder('A')