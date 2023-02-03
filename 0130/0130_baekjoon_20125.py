# https://www.acmicpc.net/problem/20125
N = int(input())
arr = [list(map(str, input())) for _ in range(N)]
bodyCount = [0] * 5

# 탐색 방향: 좌, 우, 하, 상
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
nnr = nnc = 0

for r in range(N):
    for c in range(N):
        count = 0
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < N and 0 <= nc < N and arr[nr][nc] == '*':
                count += 1
        if count == 4:
            nnr = r
            nnc = c
            print(r + 1, c + 1)
            break
# 왼팔
for i in range(nnc):
    if arr[nnr][i] == '*':
        bodyCount[0] += 1
# 오른팔
for i in range(nnc + 1, N):
    if arr[nnr][i] == '*':
        bodyCount[1] += 1
# 허리
legMark = 0
for i in range(nnr + 1, N):
    if arr[i][nnc] == '*':
        bodyCount[2] += 1
        legMark = i
# 왼다리
for i in range(N - 1, legMark, -1):
    if arr[i][nnc - 1] == '*':
        bodyCount[3] += 1
# 오른다리
for i in range(N - 1, legMark, -1):
    if arr[i][nnc + 1] == '*':
        bodyCount[4] += 1
print(*bodyCount)