class Node:
    def __init__(self,x,y):
        self.first = x
        self.second = y

# keynumber와 같은 값을 가지는 노드의 짝꿍을 찾아서 딕셔너리에 저장
def search(keynumber):
    for i in range(num-1):

        if keynumber == tree[i].first:
            if dic[keynumber] != 1:
                dic[keynumber].append(tree[i].second)

        if keynumber == tree[i].second:
            if dic[keynumber] != 1:
                dic[keynumber].append(tree[i].first)

num = int(input())
tree = []
for i in range(num-1):
    x, y= map(int, input().split())
    node = Node(x,y)
    tree.append(node)

#i값을 가진 자식의 부모노드 추리기
dic = {}
for key in range(2, num+1):
    dic[key] = []
    search(key)
    if len(dic[key]) != 1:
        if 1 in dic[key]:
            dic[key] = [1]
print(dic)
#부모 1개로 추리기
