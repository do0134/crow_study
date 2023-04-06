# BOJ 2573 빙산
# https://www.acmicpc.net/problem/2573
# python3으로 하니 시간초과, pypy3으로 하니 통과됨

# 7 7
# 0 0 0 0 0 0 0
# 0 1 1 0 1 1 0
# 0 1 9 1 9 1 0
# 0 1 1 1 1 1 0
# 0 1 1 1 1 1 0
# 0 0 1 1 1 0 0
# 0 0 0 0 0 0 0
# output : 2


from collections import deque
import copy

# 빙산 덩어리 개수 구하기
def count(x, y, num):
    q = deque()
    visited[x][y] = num
    q.append([x, y])
    while q:
        px, py = q.popleft()
        for dx, dy in dd:
            nx, ny = px + dx, py + dy
            if 0 <= nx < N and 0 <= ny < M and arr[nx][ny] != 0 and not visited[nx][ny]:
                visited[nx][ny] = num
                q.append([nx, ny])


N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
tmp = copy.deepcopy(arr)

dd = [(-1, 0), (0, 1), (1, 0), (0, -1)]
ans = 0

# 빙산 좌표 구하기
iceburg = []
for i in range(N):
    for j in range(M):
        if arr[i][j] != 0:
            iceburg.append([i, j])

while True:
    tmp_ice = []
    # 빙산 녹이기
    for x, y in iceburg:
        cnt = 0
        for dx, dy in dd:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < M and not arr[nx][ny]:
                cnt += 1
        tmp[x][y] = arr[x][y] - cnt if arr[x][y] >= cnt else 0
        if tmp[x][y] != 0:
            tmp_ice.append([x, y])
    arr = copy.deepcopy(tmp)
    iceburg = tmp_ice
    ans += 1

    # 빙산 덩어리 개수 구하기
    visited = [[0] * M for _ in range(N)]
    num = 1
    for x, y in iceburg:
        if not visited[x][y]:
            count(x, y, num)
            num += 1
    # 덩어리가 2개 이상이면
    if num > 2:
        break
    # 다 녹았으면
    if len(iceburg) == 0:
        ans = 0
        break

print(ans)