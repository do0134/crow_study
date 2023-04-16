# 프로그래머스 올바른 괄호
# https://school.programmers.co.kr/learn/courses/30/lessons/12909

def solution(s):
    l = r = 0
    for i in s :
        if i == ")" :
            r += 1
        elif i == "(" :
            l += 1
        if r > l :
            return False

    return l == r