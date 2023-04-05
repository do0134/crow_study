# BOJ 1987 알파벳
# https://www.acmicpc.net/problem/1987

def DFS(x, y, cnt):
    global maxx
    maxx = max(maxx, cnt)
    if cnt == 26:
        return
    for dx, dy in dd:
        nx, ny = x + dx, y + dy
        if 0 <= nx < R and 0 <= ny < C and not visited[nx][ny] and not alpha[ord(str(arr[nx][ny])) - 65]:
            alpha[ord(str(arr[nx][ny])) - 65] = 1
            visited[nx][ny] = 1
            DFS(nx, ny, cnt + 1)
            alpha[ord(str(arr[nx][ny])) - 65] = 0
            visited[nx][ny] = 0
    return


R, C = map(int, input().split())
visited = [[0] * C for _ in range(R)]
dd = [(-1, 0), (0, 1), (1, 0), (0, -1)]
alpha = [0] * 26
arr = [list(input()) for _ in range(R)]

visited[0][0] = 1
alpha[ord(str(arr[0][0])) - 65] = 1
maxx = 0
DFS(0, 0, 1)
print(maxx)
