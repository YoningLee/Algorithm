class Node:
    def __init__(self,value, left, right):
        self.value = value
        self.left = left
        self.right = right

def preorder(node):
    while True:
        list.append(node.value)
        if node.left:
            # node.left와 같은 값을 가진 tree[j].value가 있는 곳으로
            list.append(preorder(search(node.left)).value)

        if node.right:
            # node.right와 같은 값을 가진 tree[j].value가 있는 곳으로
            list.append(preorder(search(node.right)).value)

def search(nodevalue):
    for node in tree:
        if node.value == nodevalue:
            return node
        else:
            continue

num = int(input())
tree = []
for i in range(num):
    x, y, z = map(str, input().split())
    node = Node(x, y, z)
    tree.append(node)
list=[]

preorder(tree[0])
print(list)
