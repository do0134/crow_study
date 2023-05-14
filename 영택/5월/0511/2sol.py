# 프로그래머스 이상한 문자 만들기
# https://school.programmers.co.kr/tryouts/72053/challenges?language=python3

def solution(s):
    answer = ''
    idx = 0
    cnt = 0
    while idx < len(s) :
        if s[idx] == " " :
            answer += " "
            cnt = 0
        elif cnt % 2 :
            answer += s[idx].lower()
            cnt += 1
        elif not cnt % 2 :
            answer += s[idx].upper()
            cnt += 1
        idx += 1
    return answer