# 프로그래머스 삼각 달팽이
# https://school.programmers.co.kr/tryouts/72049/challenges?language=python3

def solution(n):
    snail = [[0] * (i + 1) for i in range(n)]
    answer = list()

    r, c = -1, 0
    value = 1
    for i in range(n) :
        for j in range(i,n) :
            if not i % 3 :
                r += 1
            elif i % 3 == 1 :
                c += 1
            else :
                r -= 1
                c -= 1
            snail[r][c] = value
            value += 1
    for i in snail :
        for j in i :
            answer.append(j)

    return answer

print(solution(20))