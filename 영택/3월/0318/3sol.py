# 프로그래머스 스킬체크 레벨 1

from collections import defaultdict

def solution(N, stages):
    answer = []
    unsolved = [0]*(N+1)
    recent = [0]*(N+1)
    for i in stages :
        if i == N+1 :
            for j in range(1,i) :
                recent[j] += 1
            continue
        for j in range(1,i+1) :
            recent[j] += 1
        unsolved[i] += 1
    fail = defaultdict(list)

    for i in range(1, N+1) :
        if not recent[i] :
            fail[0].append(i)
            continue
        fail[unsolved[i] / recent[i]].append(i)
    key = sorted(fail.keys(), reverse = True)
    for k in key :
        for i in fail[k] :
            answer.append(i)
    return answer