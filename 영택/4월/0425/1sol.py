# 프로그래머스 타겟 넘버
# https://school.programmers.co.kr/learn/courses/30/lessons/43165

def solution(numbers, target):
    global answer
    answer = 0
    backtracking(0, 0, len(numbers), target, numbers)
    return answer


def backtracking(idx, curr, n, target, numbers):
    global answer
    if idx == n:
        if curr == target:
            answer += 1
        return

    backtracking(idx + 1, curr + numbers[idx], n, target, numbers)
    backtracking(idx + 1, curr - numbers[idx], n, target, numbers)