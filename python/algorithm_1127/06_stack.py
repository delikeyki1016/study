class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.head = None
        
    def is_empty(self):
        return self.head is None
    
    def push(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
    
    def pop(self):
        if self.is_empty():
            return None
        data = self.head.data
        self.head = self.head.next
        return data
    
    def peek(self): # 맨위 확인
        if self.is_empty():
            return None
        return self.head.data 
    
stack = Stack()

stack.push('a')
stack.push('b')
stack.push('c')

# print(stack.head.next.next.data)
print(stack.peek())