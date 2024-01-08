# 이진검색트리를 전위순회한 결과가 주어졌을 때, 이 트리를 후위순회한 결과

import sys
sys.setrecursionlimit(10**6)

tree = [int(sys.stdin.readline()) for _ in range(9)]

def pre_to_post(tree):    
    def postorder(start, end):
        if start > end:
            return
        div = end + 1 # 루트노드를 기준으로 왼쪽과 오른쪽으로 서브트리를 나누기 위해 사용
        # 루트노드보다 큰 값이 나오면, 해당 노드를 기준으로 왼쪽과 오른쪽으로 서브트리를 나눔!
        for i in range(start + 1, end + 1):
            if tree[start] < tree[i]:
                div = i
                break
        postorder(start + 1, div - 1) # 왼쪽 서브트리
        postorder(div, end) # 오른쪽 서브트리
        print(tree[start]) # 중간 노드
    postorder(0, len(tree) - 1)
pre_to_post(tree)
