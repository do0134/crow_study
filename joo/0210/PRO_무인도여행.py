# PROGRAMMERS - 연습문제 - 무인도 여행
# https://school.programmers.co.kr/learn/courses/30/lessons/154540

def solution(maps):
    answer = []
    w = len(maps[0])
    h = len(maps)
    visited = [[0 for _ in range(w)] for _ in range(h)]

    def bfs(w, h, x, y, maps):
        dd = [(0, -1), (1, 0), (0, 1), (-1, 0)]
        eat = int(maps[x][y])
        q = [(x, y)]
        while q:
            px, py = q.pop(0)
            for dx, dy in dd:
                nx, ny = px + dx, py + dy
                if nx < 0 or nx >= h or ny < 0 or ny >= w or maps[nx][ny] == 'X' or visited[nx][ny]:
                    continue
                eat += int(maps[nx][ny])
                q.append((nx, ny))
                visited[nx][ny] = 1
        return eat

    for x in range(len(maps)):
        for y in range(len(maps[0])):
            if maps[x][y] == 'X' or visited[x][y]:
                continue
            visited[x][y] = 1
            answer.append(bfs(w, h, x, y, maps))
    answer.sort()
    if len(answer) == 0:
        answer = [-1]
    return answer

m1 = ["X591X","X1X5X","X231X", "1XXX1"]

print(solution(m1))