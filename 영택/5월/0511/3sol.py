# 프로그래머스 튜플
# https://school.programmers.co.kr/tryouts/72054/challenges?language=python3

def solution(s):
    answer = list()
    s = s[2:-2]
    s = s.split("},{")
    s.sort(key = len)
    for i in s:
        ii = i.split(',')
        for j in ii:
            if int(j) not in answer:
                answer.append(int(j))
    return answer