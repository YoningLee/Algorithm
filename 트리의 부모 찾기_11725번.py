class Node:
    def __init__(self,x,y):
        self.first = x
        self.second = y

# keynumber와 같은 값을 가지는 노드의 짝꿍을 찾아서 딕셔너리에 저장
def search(keynumber):
    for i in range(num-1):
        print(keynumber, tree[i].first)
        if keynumber == tree[i].first:
            print(keynumber, tree[i].first)
            dic[keynumber] = tree[i].second
        print(keynumber, tree[i].second)
        if keynumber == tree[i].second:
            print(keynumber, tree[i].second)
            dic[keynumber] = tree[i].first
    print(dic)

num = int(input())
tree = []
for i in range(num-1):
    x, y= map(int, input().split())
    node = Node(x,y)
    tree.append(node)

#i값을 가진 자식의 부모노드 추리기
dic = {}
for key in range(2,num+1):
    search(key)
print(dic)
