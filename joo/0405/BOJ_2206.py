# BOJ 2206 벽 부수고 이동하기
# https://www.acmicpc.net/problem/2206

# 시간초과난 코드
# from collections import deque

#
# def BFS(x, y):
#     global minn
#     q = deque([(x, y)])
#     visited[x][y] = 1
#     while q:
#         px, py = q.popleft()
#         if visited[px][py] >= minn:
#             return
#         for dx, dy in dd:
#             nx, ny = px + dx, py + dy
#             if 0 <= nx < N and 0 <= ny < M and not arr[nx][ny] and not visited[nx][ny]:
#                 q.append((nx, ny))
#                 visited[nx][ny] = visited[px][py] + 1
#                 if nx == N-1 and ny == M-1:
#                     minn = min(minn, visited[nx][ny])
#                     return
#
# N, M = map(int, input().split())
# arr = [list(map(int, input().strip())) for _ in range(N)]
# dd = [(-1, 0), (0, 1), (1, 0), (0, -1)]
# minn = 1000 * 1000 + 1
# # 부술 벽 정하기 + BFS 돌리기
# for i in range(N):
#     for j in range(M):
#         if arr[i][j]:
#             arr[i][j] = 0
#             visited = [[0] * M for _ in range(N)]
#             BFS(0, 0)
#             arr[i][j] = 1
#
# print(minn if minn < 1000001 else -1)



from collections import deque

N, M = map(int, input().split())
arr = [list(map(int, input().strip())) for _ in range(N)]
dd = [(-1, 0), (0, 1), (1, 0), (0, -1)]

# 3차원으로 visited[x][y][0] 은 안 부순 상태에서의 방문 visited[x][y][1]은 부순 상태에서의 방문
def bfs(x, y):
    q = deque()
    q.append([x, y, 0])
    visited = [[[0] * 2 for _ in range(M)] for _ in range(N)]
    visited[0][0][0] = 1
    while q:
        px, py, pw = q.popleft()
        if px == N - 1 and py == M - 1:
            return visited[px][py][pw]

        for dx, dy in dd:
            nx, ny = px + dx, py + dy
            if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny][pw]:
                if arr[nx][ny] == 0:
                    visited[nx][ny][pw] = visited[px][py][pw] + 1
                    q.append([nx, ny, pw])
                elif pw == 0:
                    visited[nx][ny][1] = visited[px][py][pw] + 1
                    q.append([nx, ny, 1])
    return -1


print(bfs(0, 0))
