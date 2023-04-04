# BOJ 다리 만들기
# https://www.acmicpc.net/problem/2146

from collections import deque

dd = [(-1, 0), (0, 1), (1, 0), (0, -1)]

def BFS(x, y, num):
    visit = [[0] * N for _ in range(N)]
    lst = [(x, y)]
    qq = deque([(x, y)])
    table[x][y] = num
    while qq:
        bnx, bny = qq.popleft()
        for dx, dy in dd:
            bpx, bpy = bnx + dx, bny + dy
            if 0 <= bpx < N and 0 <= bpy < N and table[bpx][bpy] and not visit[bpx][bpy]:
                visit[bpx][bpy] = 1
                table[bpx][bpy] = num
                lst.append((bpx, bpy))
                qq.append((bpx, bpy))
    return lst


N = int(input())
table = []
ans = 201
for i in range(N):
    lst = list(map(int, input().split()))
    table.append(lst)

# 섬 구분하기
num = 2
start_xy = []
for i in range(N):
    for j in range(N):
        if table[i][j] == 1:
            start_xy.append(BFS(i, j, num))
            num += 1

for n in range(2, num):
    visited = [[0] * N for _ in range(N)]
    q = deque()
    minn = 201
    flag = 0
    for kx, ky in start_xy[n-2]:
        q.append((kx, ky))
        visited[kx][ky] = 1
    while q:
        nx, ny = q.popleft()
        for dx, dy in dd:
            px, py = nx + dx, ny + dy
            if 0 <= px < N and 0 <= py < N:
                if table[px][py] != 0 and table[px][py] != n:
                    minn = visited[nx][ny] - 1
                    flag = 1
                    break
                if table[px][py] == 0 and not visited[px][py]:
                    visited[px][py] = visited[nx][ny] + 1
                    q.append((px, py))
        if flag:
            break
    ans = min(ans, minn)

print(ans)


