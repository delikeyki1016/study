# https://www.acmicpc.net/problem/1158
# N명의 사람이 원을 이루고 앉아있고, 양의정수K가 주어졌다. K번째부터 삭제됨. 이후 다시 K번째 삭제됨. 

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
        current.next = Node(value)
    
    def get_node(self, index):
        current = self.head
        count = 0
        while count < index:
            count += 1
            current = current.next
        return current
    
    def delete(self, index):
        if index == 0:
            del_node = self.head.data
            self.head = self.head.next
            return del_node
        node = self.get_node(index - 1)
        del_node = node.next.data
        node.next = node.next.next
        return del_node
    
import sys

N, K = [int(i) for i in sys.stdin.readline().split()] # N 전체인원 K번째 사람부터 킬

# 연결리스트 세팅(1~N까지 숫자 삽입)
ll = LinkedList(1)
for i in range(2, N+1):
    ll.insert(i)
    
# 요세프스 순열 만들기
josephus = []
idx = K - 1 # 지워야하는 인덱스

while ll.head.next is not None:
    print(idx, K, N)
    idx %= N # 한명이 죽으면 그다음 idx는 전체를 나눈 나머지값이 그 다음 idx
    died_person = ll.delete(idx)
    josephus.append(died_person)
    idx += K - 1
    N -= 1 # 한명이 죽으니깐 전체에서 빼주고

# josephus.append(ll.head.data) # 마지막 남은 한 명 추가, 아래로도 가능 
josephus.append(ll.delete(0))

# print(josephus)
result = '<'
for i in josephus:
    if i != josephus[-1]:
        result += str(i) + ", "
    else:
        result += str(i) + ">"
                
print(result)