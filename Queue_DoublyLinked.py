from DoublyLinkedList import Node
from DoublyLinkedList import DoublyLinkedList

class LinkedListQueue:

    def __init__(self):
        self.data = DoublyLinkedList()

    def size(self):
        return self.data.getLength()

    def isEmpty(self):
        return self.data.getLength()==0

    def enqueue(self, item):
        node = Node(item)
        self.data.insertAt(self.data.nodeCount+1, node)

    def dequene(self):
        return self.data.popAt(1)

    def peek(self):
        return (self.data.getAt(1)).data

