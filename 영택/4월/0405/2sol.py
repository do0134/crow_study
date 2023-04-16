# 프로그래머스 전력망을 둘로 나누기
# https://school.programmers.co.kr/learn/courses/30/lessons/86971

from collections import deque

'''
Union Find를 쓰면 매우 빨라진다고 한다...
'''
def bfs(s, a, b, n):
    tree[a][b] = 0
    tree[b][a] = 0

    v = [0] * (n + 1)
    q = deque()
    q.append(s)
    v[s] = 1
    cnt = 0
    while q:
        now = q.popleft()
        for i in range(n + 1):
            if tree[now][i] and not v[i]:
                q.append(i)
                cnt += 1
                v[i] = 1
    tree[a][b] = 1
    tree[b][a] = 1
    return cnt


def solution(n, wires):
    global tree

    answer = int(1e9)
    tree = [[0] * (n + 1) for _ in range(n + 1)]

    for a, b in wires:
        tree[a][b] = 1
        tree[b][a] = 1

    for v1, v2 in wires:
        cnt1 = bfs(v1, v1, v2, n)
        cnt2 = bfs(v2, v1, v2, n)
        answer = min(abs(cnt1 - cnt2), answer)

    return answer