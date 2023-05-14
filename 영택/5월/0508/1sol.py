# 프로그래머스 행렬 테두리 회전하기
# https://school.programmers.co.kr/tryouts/72048/challenges?language=python3
def solution(rows, columns, queries):
    value = 1
    array = [[0] * columns for _ in range(rows)]
    for i in range(rows):
        for j in range(columns):
            array[i][j] = value
            value += 1
    answer = []
    for query in queries:
        sr, sc, er, ec = query
        sr, sc, er, ec = sr - 1, sc - 1, er - 1, ec - 1
        start = array[sr][sc]
        next_value = array[sr][sc]
        before_value = array[sr][sc]
        min_v = start
        for i in range(sc + 1, ec + 1):
            next_value = array[sr][i]
            array[sr][i] = before_value
            before_value = next_value
            min_v = min(min_v, before_value)

        for i in range(sr + 1, er + 1):
            next_value = array[i][ec]
            array[i][ec] = before_value
            before_value = next_value
            min_v = min(min_v, before_value)

        for i in range(ec - 1, sc - 1, -1):
            next_value = array[er][i]
            array[er][i] = before_value
            before_value = next_value
            min_v = min(min_v, before_value)

        for i in range(er - 1, sr - 1, -1):
            next_value = array[i][sc]
            array[i][sc] = before_value
            before_value = next_value
            min_v = min(min_v, before_value)

        answer.append(min_v)

    return answer