# 중위 순회

class Node:
    def __init__(self, data, left, right):
        self.data = data
        self.left = left
        self.right = right 

# 중위순회는 좌측 -> 루트 -> 우측
def inorder(node):
    if node.left != ".":
        inorder(tree[node.left])
    print(node.data, end=" ")
    if node.right != ".":
        inorder(tree[node.right])    
        
        
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

inorder(tree['A'])