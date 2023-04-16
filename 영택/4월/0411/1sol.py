# 프로그래머스 H-Index
# https://school.programmers.co.kr/learn/courses/30/lessons/42747

def solution(citations):
    citations.sort()
    answer = 0
    for i in range(len(citations)) :
        if citations[i] >= len(citations) - i :
            answer += 1
    return answer