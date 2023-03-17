# programmers 연습문제 - 혼자 놀기의 달인
# https://school.programmers.co.kr/learn/courses/30/lessons/131130

def solution(cards):
    answer = 0
    visited = [0 for _ in range(len(cards))]
    cnts = []
    now = 0
    while visited.count(0) != 0:
        for i in range(len(cards)):
            if visited[i] == 0:
                now = i
                break
        cnt = 0
        while visited[now] == 0:
            visited[now] = 1
            now = cards[now] - 1
            cnt += 1
        cnts.append(cnt)
    cnts.sort(reverse=True)
    if len(cnts) == 1:
        answer = 0
    else:
        answer = cnts[0] * cnts[1]
    return answer


c1 = [8, 6, 3, 7, 2, 5, 1, 4]
print(solution(c1))
