import itertools

def solution(n, m, x, y, r, c, k):
    answer = 'impossible'
    letter = ['d', 'l', 'r', 'u']
    dd = {'l': (0, -1), 'r': (0, 1), 'u': (-1, 0), 'd': (1, 0)}
    kinds = list(itertools.product(letter, repeat=k))

    for kind in kinds:
        flag = 0
        nx, ny = x, y
        for kd in kind:
            nx, ny = nx + dd[kd][0], ny + dd[kd][1]
            if nx < 1 or nx > n or ny < 1 or ny > m:
                flag = 1
                break
        if flag:
            continue
        if nx == r and ny == c:
            return ''.join(kind)

    return answer