# 프로그래머스 입국심사
# https://school.programmers.co.kr/learn/courses/30/lessons/43238

def solution(n, times):
    answer = 0
    l = min(times)
    r = l*n
    while l+1 != r :
        mid = (l+r) // 2
        value = 0
        for time in times :
            value += mid // time
            if value >= n :
                r = mid
                break
        else :
            l = mid

    return r