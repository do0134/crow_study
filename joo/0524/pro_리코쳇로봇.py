from collections import deque


def solution(board):
    length = len(board)
    width = len(board[0])
    answer = 0
    dd = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    ri, rj = 0, 0
    for i in range(length):
        for j in range(width):
            if board[i][j] == "R":
                ri, rj = i, j

    def bfs(x, y):
        q = deque()
        q.append((x, y))
        visited = [[0] * width for _ in range(length)]
        visited[x][y] = 1

        while q:
            px, py = q.popleft()
            if board[px][py] == "G":
                return visited[px][py]
            for di, dj in dd:
                nx, ny = px, py
                while True:
                    nx, ny = nx + di, ny + dj
                    if 0 <= nx < length and 0 <= ny < width and board[nx][ny] == "D":
                        nx -= di
                        ny -= dj
                        break
                    if nx < 0 or nx >= length or ny < 0 or ny >= width:
                        nx -= di
                        ny -= dj
                        break
                if not visited[nx][ny]:
                    visited[nx][ny] = visited[px][py] + 1
                    q.append((nx, ny))
        return -1

    answer = bfs(ri, rj)
    if answer > 0:
        answer -= 1

    return answer


b1 = ["...D..R", ".D.G...", "....D.D", "D....D.", "..D...."]
print(solution(b1))
