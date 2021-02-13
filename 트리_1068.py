num = int(input())
parent = list(map(int, input().split()))
delnode = int(input())
#tree 딕셔너리의 key=노드번호, value=해당 노드의 부모노드번호
tree = {}
for node, parentvalue in enumerate(parent):
    tree[node] = parentvalue
#삭제할 노드가 0이면 leafnode는 없으므로 바로 0출력
if delnode == 0:
    print(0)
else:
    queue = [] #방문해야 할 노드를 저장할 큐
    tree[delnode]='x'#해당노드 무효화
    queue.append(delnode) #delnode를 부모노드로 가지는 노드 방문예정
    while queue!=[]: #방문해야 하는 노드가 없을 때까지 반복
        hint = queue.pop(0)
        count= 0
        for i in range(delnode, num):
            #hint를 부모노드로 가지는 노드 무효화
            if tree[i] == hint:
                tree[i]='x'
                queue.append(i)
                count+=1
            #이진트리이므로 한 부모에 검사할 노드를 2이하로 제한
            if count==2:
                break

    leaf_count=0
    for value in range(1, num):
        #유효한 노드만 leaf후보로 카운트
        if tree[value] != 'x':
            leaf_count+=1
        #무효노드인 경우 break
        else:
            break
        #유효한 노드에 한해서 해당 노드를 부모로 가지는 다른 노드가 있나 검사
        for j in range(value+1, num):
            #해당 노드를 부모로 가지는 노드가 있을 경우
            if tree[j] == value:
                #leaf후보에서 제외, leafcount 1감소
                leaf_count-=1
                break
    print(leaf_count)