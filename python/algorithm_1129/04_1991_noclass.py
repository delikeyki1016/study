import sys

def preorder(node):
    print(node, end="")
    if tree[node][0] != ".":
        preorder(tree[node][0])
    if tree[node][1] != ".":
        preorder(tree[node][1])

def inorder(node):
    if tree[node][0] != ".":
        inorder(tree[node][0])
    print(node, end="")
    if tree[node][1] != ".":
        inorder(tree[node][1])

def postorder(node):
    if tree[node][0] != ".":
        postorder(tree[node][0])
    if tree[node][1] != ".":
        postorder(tree[node][1])
    print(node, end="")
    
N = int(sys.stdin.readline())
tree = {}
for _ in range(N):
    data, left, right = sys.stdin.readline().split() 
    tree[data] = (left, right)
# tree = {'A': ('B', 'C'), 'B': ('D', '.'), 'C': ('E', 'F'), 'E': ('.', '.'), 'F': ('.', 'G'), 'D': ('.', '.'), 'G': ('.', '.')}

preorder('A')
print()
inorder('A')
print()
postorder('A')