import sys
sys.setrecursionlimit(5000)

letter = ['d', 'l', 'r', 'u']
dd = [(1, 0), (0, -1), (0, 1), (-1, 0)]


def dfs(x, y, n, m, r, c, k, sent, diff):
    global answer
    if k == 0 and diff == 0:
        answer = sent
        return True

    for i in range(4):
        nx, ny = x + dd[i][0], y + dd[i][1]
        if 0 <= nx < n and 0 <= ny < m and diff <= k:
            if diff % 2 == k % 2:
                if (dfs(nx, ny, n, m, r, c, k - 1, sent + letter[i],
                        abs(r - nx) + abs(c - ny))):
                    return True
    return False


def solution(n, m, x, y, r, c, k):
    global answer
    answer = ''
    dfs(x - 1, y - 1, n, m, r - 1, c - 1, k, '', abs(r - x) + abs(c - y))
    if answer == '':
        return 'impossible'

    return answer


print(solution(3, 4, 2, 3, 3, 1, 5))
