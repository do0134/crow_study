# https://www.acmicpc.net/problem/14940
# bfs 기본
from collections import deque
import sys

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
def bfs(x, y):
    q = deque([(x, y)])
    visitedArr[x][y] = 0
    while q:
        x, y = q.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < N and 0 <= ny < M and visitedArr[nx][ny] == -1:
                if arr[nx][ny] == 0:
                    visitedArr[nx][ny] = 0
                elif arr[nx][ny] == 1:
                    q.append((nx, ny))
                    visitedArr[nx][ny] = visitedArr[x][y] + 1

N, M = map(int, sys.stdin.readline().split())
# N, M 바꿔서 계속 인덱스 에러 났다,,,,몽충이
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
visitedArr = [[-1] * M for _ in range(N)]
count = 0
for i in range(N):
    for j in range(M):
        if arr[i][j] == 2 and visitedArr[i][j] == -1:
            bfs(i, j)
# 접근 불가 지역일 때 (방문하지 않은 갈 수 있는 땅 => 0에 둘러쌓인 곳)
for i in range(N):
    for j in range(M):
        if arr[i][j] == 0:
            print(0, end=" ")
        else:
            print(visitedArr[i][j], end=" ")
    print()