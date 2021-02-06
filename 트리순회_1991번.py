class Node:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None
class Queue:
    def __init__(self):
        self.data=[]

class BinaryTree:
    def __init__(self):
        self.root = Node(None)
    def insert(self, root, left, right):
        self.current_node = self.root
        depth=0
        while True:
            if(self.current_node.value == None):
                self.current_node.value = root
                self.current_node.left = left
                self.current_node.right = right
                break
            elif((self.current_node.left.value != root)and(self.current_node.right.value != root)):
                #이진트리에 root과 같은 값을 가진 노드 찾기

            else:
                if(self.current_node.left.value == root):
                    self.current_node = self.current_node.left
                    self.current_node.left = left
                    self.current_node.right = right
                    break
                elif(self.current_node.right.value == root):
                    self.current_node = self.current_node.right
                    self.current_node.left = left
                    self.current_node.right = right
                    break
    def search(self, value):
        self.current_node = self.root


num = int(input())
tree = []
for i in range(num):
    list = []
    list = (str(x) for x in input().split())
    tree.append(list)
Q=[]Queue
BT = BinaryTree()
for i in range(num):
    BT.insert(tree[i][0], tree[i][1], tree[i][2])
첫 번째 목표: 이진트리 생성하기
