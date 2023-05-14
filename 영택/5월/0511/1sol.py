# 프로그래머스 시저암호
# https://school.programmers.co.kr/tryouts/72052/challenges

def solution(s, n):
    answer = ''
    for i in s:
        if i == " ":
            answer += " "
        elif 65 <= ord(i) <= 90:
            temp = ord(i) + n
            if temp > 90:
                temp = 65 + temp - 91
            answer += chr(temp)
        elif 97 <= ord(i) <= 122:
            temp = ord(i) + n
            if temp > 122:
                temp = 97 + temp - 123
            answer += chr(temp)

    return answer