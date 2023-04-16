# 프로그래머스 폰켓몬
# https://school.programmers.co.kr/learn/courses/30/lessons/1845

def solution(nums):
    n = len(nums)
    m = len(set(nums))
    if m >= n / 2 :
        return n//2
    return m