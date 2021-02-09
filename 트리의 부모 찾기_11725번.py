class Node:
    def __init__(self,x,y,z):
        self.parent = x
        self.child = y
        self.child2 = z

num = int(input())
tree = []
for i in range(num):
    x, y= map(str, input().split())
    node = Node(x,y,None)
    tree.append(node)
keynumber=2
def nodemate():
    while True:
        
        if keynumber in tree[i]