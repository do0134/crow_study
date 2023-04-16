# 프로그래머스 연속된 부분 수열의 합
# https://school.programmers.co.kr/learn/courses/30/lessons/178870

def solution(s, k):
    if s[0] == k:
        return [0, 0]
    l = 0
    r = 1
    value = s[0] + s[1]
    answer = []
    while r < len(s):
        if value < k:
            r += 1
            if r == len(s):
                break
            value += s[r]
        elif value > k:
            value -= s[l]
            l += 1
            if l == r:
                if value == k:
                    return [l, r]
                r += 1
                if r == len(s):
                    break
                value += s[r]
        elif value == k:
            if not answer:
                answer = [l, r]
            elif answer[1] - answer[0] > r - l:
                answer = [l, r]
            r += 1
            if r == len(s):
                break
            value += s[r]

    return answer