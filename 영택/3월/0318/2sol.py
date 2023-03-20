# 프로그래머스 스킬체크 레벨 1

def solution(s):
    s = sorted(list(s), reverse = True)
    answer = ""
    for i in s :
        answer += i

    return answer