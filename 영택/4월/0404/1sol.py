# 프로그래머스 괄호변환
# https://school.programmers.co.kr/learn/courses/30/lessons/60058#

def solution(p):
    def check(string):
        l = r = 0
        for i in string:
            if i == "(":
                l += 1
            else:
                r += 1
            if r > l:
                return False
        return True

    def change(string):
        value = ""
        if check(string):
            return string

        for i in range(1, len(string) - 1):
            if string[i] == "(":
                value += ")"
            else:
                value += "("
        return value

    def dq(string):
        if not string:
            return ""

        l = r = 0

        for i in range(len(string)):
            if string[i] == "(":
                l += 1
            else:
                r += 1
            if l == r:
                left = string[:i + 1]
                right = string[i + 1:]
                break
        return left, right

    def answer(string):
        if not string:
            return ""

        if check(string):
            return string

        left, right = dq(string)

        if check(left):
            value = left + answer(right)

        else:
            value = "(" + answer(right) + ")" + change(left)

        return value

    return answer(p)