class Node:
    def __init__(self,value, left, right):
        self.value = value
        self.left = left
        self.right = right
class Queue:
    def __init__(self):
        self.data = []

    def isEmpty(self):
        if len(self.data)==0:
            return True
        else:
            return False
    def enqueue(self, value):
        return self.data.append(value)

    def dequeue(self):
        return self.data.pop(0)

    def peek(self):
        return self.data[0]

class BinaryTree:
    def __init__(self):
        self.root = Node(value, left, right)
    def insert(self, newnode, start):
        self.curr = start
        while True:
            if self.curr.value == None:
                self.curr.value = newnode.value
                self.curr.left = newnode.left
                self.curr.right = newnode.right
                break
            else:
                self.curr.left = newnode.left
                self.curr.right = newnode.right
                break
    def currSearch(self,keynode):
        self.curr = self.root
        if self.curr.value == keynode.value:
            return self.curr
        else:
            if self.curr.left:
                if self.curr.left == keynode.value:
                    return self.curr.left
                else:
                    self.curr.left.currSearch(keynode)
num = int(input())
tree = []
Q = Queue()
for i in range(num):
    x, y, z = map(str, input().split( ))
    if y == '.':
        y = None
    if z == '.':
        y = None
    node = Node(x, y, z)
    tree.append(node)
BT = BinaryTree()
i=0
for i in range(num):
    if not Q.isEmpty():
        start = Q.dequeue()
    else:
        start = Node(None)

    node = tree[i]
    BT.insert(node, start)
    if node.left != None:
        Q.enqueue(Node(node.left))
    if node.right != None:
        Q.enqueue(Node(node.right))
