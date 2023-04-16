# 프로그래머스 기능개발
# https://school.programmers.co.kr/learn/courses/30/lessons/42586?language=python3
def solution(progresses, speeds):
    n = len(speeds)
    temp = list()
    for i in range(n):
        if (100 - progresses[i]) % speeds[i]:
            temp.append((100 - progresses[i]) // speeds[i] + 1)
        else:
            temp.append((100 - progresses[i]) // speeds[i])

    day = temp[0]
    answer = []
    answer.append(1)
    for i in range(1, n):
        if day < temp[i]:
            answer.append(1)
            day = temp[i]
        else:
            answer[-1] += 1
    return answer