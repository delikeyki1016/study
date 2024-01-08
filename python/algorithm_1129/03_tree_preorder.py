# 전위 순회

class Node:
    def __init__(self, data, left, right):
        self.data = data
        self.left = left
        self.right = right 

# 전위순회는 루트 -> 좌측 -> 우측
def preorder(node):
    print(node.data, end=" ")
    if node.left != ".":
        preorder(tree[node.left])
    if node.right != ".":
        preorder(tree[node.right])    
        
        
tree = {
    'A' : Node('A', 'B', 'C'),
    'B' : Node('B', 'D', 'E'),
    'C' : Node('C', 'F', 'G'),
    'D' : Node('D', 'H', '.'),
    'E' : Node('E', '.', '.'),
    'F' : Node('F', '.', '.'),
    'G' : Node('G', '.', '.'),
    'H' : Node('H', '.', '.'),
}

preorder(tree['A'])