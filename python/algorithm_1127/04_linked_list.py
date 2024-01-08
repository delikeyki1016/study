# 선형자료구조 - 연결리스트 코드 구현하기

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
class LinkedList:
    def __init__(self, value):
        self.head = Node(value)
    
    def insert(self, value):
        current = self.head
        while current.next is not None:
            current = current.next
        current.next = Node(value) # 현재의 넥스트를 insert한 Node를 넣음
        
    def get_node(self, index): # index값 가져오기
        current = self.head
        count = 0
        while count < index:
            count += 1
            current = current.next
        return current
    
    def delete(self, index): # index값 삭제
        if index == 0: # 첫번째것 삭제인 경우 
            del_node = self.head.data 
            self.head = self.head.next
            return del_node
        else:
            node = self.get_node(index - 1)
            del_node = node.next.data
            node.next = node.next.next
            return del_node
        
    # def __str__(self):
    #     return self.head.data
            
ll = LinkedList('a')
ll.insert('b')
ll.insert('c')
ll.insert('d')

# print(ll)
# print(ll.head)
# print(ll.head.data)
# print(ll.head.next.data)
# print(ll.head.next.next.data)
# print(ll.head.next.next.next.data)
# print(ll.get_node(2).data)
print(ll.delete(2))
print(ll.head.next.next.data)

# sam code 
# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None

# class LinkedList:
#     def __init__(self, value):
#         self.head = Node(value)
    
#     def insert(self, value):
#         current = self.head
#         while current.next is not None:
#             current = current.next
#         current.next = Node(value)
    
#     def get_node(self, index):
#         current = self.head
#         count = 0
#         while count < index:
#             count += 1
#             current = current.next
#         return current
    
#     def delete(self, index):
#         if index == 0:
#             del_node = self.head.data
#             self.head = self.head.next
#             return del_node
#         node = self.get_node(index - 1)
#         del_node = node.next.data
#         node.next = node.next.next
#         return del_node