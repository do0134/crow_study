# 프로그래머스 가장 긴 팰린드롬
# https://school.programmers.co.kr/learn/courses/30/lessons/12904

def check(s):
    l = 0
    r = len(s) - 1
    while l < r:
        if s[l] != s[r]:
            return False
        l += 1
        r -= 1
    return True


def solution(s):
    answer = 1

    for i in range(len(s) - 1):
        for j in range(len(s) - 1, i, -1):
            if s[i] == s[j] and j - i + 1 > answer:
                if check(s[i:j + 1]):
                    answer = max(answer, j - i + 1)
    return answer