num = int(input())
list = []
for i in range(num):
    x, y = map(int, input().split())
    k = 0
    d = y - x - 1
    while (k * (k + 1)) / 2 < d:
        k += 1
    list.append(k+1)

for i in range(num):
    print(list[i])