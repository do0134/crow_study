# PROGRAMMERS - 연습문제 - 숫자 변환하기
# https://school.programmers.co.kr/learn/courses/30/lessons/154538


from collections import deque


def solution(x, y, n):
    def bfs(x, y, n):
        q = deque()
        dist[x] = 1
        q.append(x)

        while q:
            x = q.popleft()
            if 0 <= x + n <= 10 ** 6 and dist[x + n] == 0:
                dist[x + n] = dist[x] + 1
                q.append(x + n)
            if 0 <= x * 2 <= 10 ** 6 and dist[x * 2] == 0:
                dist[x * 2] = dist[x] + 1
                q.append(x * 2)
            if 0 <= x * 3 <= 10 ** 6 and dist[x * 3] == 0:
                dist[x * 3] = dist[x] + 1
                q.append(x * 3)

    dist = [0] * 1000001
    bfs(x, y, n)

    return dist[y] - 1


x1, y1, n1 = 10, 40, 5
x2, y2, n2 = 10, 40, 30
print(solution(x2, y2, n2))
