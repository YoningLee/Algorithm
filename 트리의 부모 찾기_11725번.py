import collections
class Node():
    def __init__(self, data):
        self.data = data
        self.child = []
        self.parent = None
N=int(input())
tree = {}
for i in range(N-1):
    n1,n2=map(int, input().split())
    if n1 not in tree:
        tree[n1]=Node(n1)
    tree[n1].child.append(n2)
    #n2가 tree의 key값인지 검사
    if n2 not in tree:
        tree[n2]=Node(n2)
    tree[n2].child.append(n1)
queue = collections.deque([1])
while len(queue)!=0:
    front=queue.popleft()
    if tree[front].child==[]:
        continue
    else:
        for ch in tree[front].child:
            if ch!=tree[front].parent:
                tree[ch].parent=front
                queue.append(ch)
for i in range(2,N+1):
    print(tree[i].parent)
