# 프로그래머스 연습문제 - 미로 탈출
# https://school.programmers.co.kr/learn/courses/30/lessons/159993

from collections import deque


def BFS(m, w, l, sx, sy, ex, ey, ):
    dd = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    visited = [[0 for _ in range(w)] for _ in range(l)]
    q = deque()
    q.append((sx, sy))
    visited[sx][sy] = 1
    while q:
        nx, ny = q.popleft()
        if (nx, ny) == (ex, ey):
            return visited[ex][ey] - 1
        for dx, dy in dd:
            cx, cy = nx + dx, ny + dy
            if 0 <= cx < l and 0 <= cy < w and m[cx][cy] != "X" and (
                    visited[cx][cy] > (visited[nx][ny] + 1) or visited[cx][cy] == 0):
                visited[cx][cy] = visited[nx][ny] + 1
                q.append((cx, cy))
    return -1


def solution(maps):
    answer = 0
    w = len(maps[0])
    l = len(maps)
    sx = sy = ex = ey = lx = ly = 0
    for i in range(l):
        for j in range(w):
            if maps[i][j] == "S":
                sx, sy = i, j
            elif maps[i][j] == "E":
                ex, ey = i, j
            elif maps[i][j] == "L":
                lx, ly = i, j
    laber = BFS(maps, w, l, sx, sy, lx, ly)
    if laber == -1:
        return -1
    answer += laber

    exit = BFS(maps, w, l, lx, ly, ex, ey)
    if exit == -1:
        return -1
    answer += exit
    return answer


m1 = ["SOOOL", "XXXXO", "OOOOO", "OXXXX", "OOOOE"]
m2 = ["LOOXS", "OOOOX", "OOOOO", "OOOOO", "EOOOO"]
print(solution(m1))
