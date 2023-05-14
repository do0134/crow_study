# 프로그래머스 짝지어 제거하기
# https://school.programmers.co.kr/tryouts/72055/challenges

def solution(s):
    idx = 0
    stack = list()
    while idx < len(s):
        if not stack or stack[-1] != s[idx]:
            stack.append(s[idx])
            idx += 1
        elif stack[-1] == s[idx]:
            stack.pop()
            idx += 1
    if stack:
        return 0
    else:
        return 1