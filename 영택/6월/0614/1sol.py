# 백준 1976 여행가자
# https://www.acmicpc.net/problem/1976

n = int(input())
m = int(input())
city = [[0]]
parent = [0]

for i in range(1,n+1) :
    city.append([0] + list(map(int,input().split())))
    parent.append(i)

plan = list(map(int,input().split()))
rank = [0]*(n+1)


def find(x) :
    if parent[x] != x :
        parent[x] = find(parent[x])
    return parent[x]


def union(x, y) :
    x_root = find(x)
    y_root = find(y)
    if x_root == y_root :
        return

    if rank[x_root] < rank[y_root] :
        parent[x_root] = y_root
    elif rank[x_root] > rank[y_root] :
        parent[y_root] = x_root
    else :
        parent[y_root] = x_root
        rank[x_root] += 1


connect = list()
for i in range(1, n+1) :
    for j in range(1, n+1) :
        if city[i][j] == 1 :
            connect.append((i, j))

for i,j in connect :
    union(i, j)

check = find(plan[0])

for i in range(1,m) :
    visit = find(plan[i])
    if visit != check :
        print("NO")
        break
else :
    if check == visit :
        print("YES")
    else :
        print("NO")