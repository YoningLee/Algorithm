num = int(input())
tree={}
for i in range(num):
    x, y, z = map(str, input().split())
    if y == '.':
        y = None
    if z == '.':
        z = None
    tree[x] = list((y,z))
tree_copy = tree
print(tree)