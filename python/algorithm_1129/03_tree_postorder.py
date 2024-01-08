# 후위 순회

class Node:
    def __init__(self, data, left, right):
        self.data = data
        self.left = left
        self.right = right 

# 후위순회는  좌측 -> 우측 -> 루트 
def postorder(node):
    if node.left != ".":
        postorder(tree[node.left])
    if node.right != ".":
        postorder(tree[node.right])
    print(node.data, end=" ")

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

postorder(tree['A'])