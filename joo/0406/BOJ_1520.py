# BOJ 1520 내리막길
# https://www.acmicpc.net/problem/1520
# 시간 초과 먼데,,,, ㅎ ㅏ 울고 싶다
import sys
sys.setrecursionlimit(10**8)

def DFS(x, y):
    global answer
    if x == M-1 and y == N-1:
        dp[x][y] = 1
        return 1

    if dp[x][y] != -1 and dp[x][y] != 0:
        return dp[x][y]

    answer = 0
    for dx, dy in dd:
        nx, ny = x + dx, y + dy
        if 0 <= nx < M and 0 <= ny < N and arr[x][y] > arr[nx][ny]:
            answer += DFS(nx, ny)

    dp[x][y] = answer
    return dp[x][y]


M, N = map(int, sys.stdin.readline().split())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(M)]
dd = [(-1, 0), (0, 1), (1, 0), (0, -1)]
answer = 0
dp = [[-1] * N for _ in range(M)]

print(DFS(0, 0))

