# 선형자료구조 - 큐 : 다음에 처리할 목표를 쌓아두기

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
class Queue:
    def __init__(self, data):
        self.head = Node(data)
        self.tail = self.head
        
    def is_empty(self):
        return self.head is None
    
    def enqueue(self, data): # 노드 추가
        new_node = Node(data)
        self.tail.next = new_node # 현재 꼬리의 넥스트를 신규 노드로 연결
        self.tail = new_node # 현재 꼬리를 신규 노드로 선언 
        
    def dequeue(self):
        if self.is_empty():
            return None
        data = self.head.data # 현재의 값을 일단 저장해두고 
        self.head = self.head.next # 현재 헤드가 그 다음 값으로 변경
        return data # 저장해둔 값을 리턴 
    
    def peek(self):
        if self.is_empty():
            return None
        return self.head.data
        
        
        
