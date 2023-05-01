# 프로그래머스 최댓값과 최솟값
# https://school.programmers.co.kr/learn/courses/30/lessons/12939
def solution(s):
    s = list(map(int,s.split()))
    answer = str(min(s)) + " " + str(max(s))
    return answer