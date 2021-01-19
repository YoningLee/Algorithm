from DoublyLinkedList import Node
from DoublyLinkedList import DoublyLinkedList

class PriorityQueue:

    def __init__(self):
        self.queue = DoublyLinkedList()

    def size(self):
        return self.queue.getLength()

    def isEmpty(self):
        return self.size() == 0

    def enqueue(self, x):
        newNode = Node(x)
        curr = self.queue.head
        #x가 큰 순서대로 나열되는 연결리스트
        while curr.next!=self.queue.tail and x < curr.next.data:
            curr = curr.next
        self.queue.insertAfter(curr, newNode)

    def dequeue(self):
        return self.queue.popAt(self.queue.getLength()) #마지막노드 데이터 리턴

    def peek(self):
        return self.queue.getAt(self.queue.getLength()).data