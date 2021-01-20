class ArrayQueue:

    def __init__(self):
        self.data = []

    def size(self):
        return len(self.data)

    def isEmpty(self):
        return self.size() == 0

    def enqueue(self, item):
        self.data.append(item)

    def dequeue(self):
        return self.data.pop(0)

    def peek(self):
        return self.data[0]


class Node:

    def __init__(self, item):
        self.data = item
        self.left = None
        self.right = None


class BinaryTree:

    def __init__(self, r):
        self.root = r

    def bft(self): #넓이 우선 순회
        traversal = []
        Q = ArrayQueue()

        if self.root:
            Q.enqueue(self.root)

        while not Q.isEmpty():
            node = Q.dequeue()
            traversal.append(node.data)
            if node.left:
                Q.enqueue(node.left)
            if node.right:
                Q.enqueue(node.right)

        return traversal