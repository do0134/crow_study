# 프로그래머스 오픈채팅방
# https://school.programmers.co.kr/learn/courses/30/lessons/42888

from collections import defaultdict


def solution(record):
    answer = []
    a = "님이 들어왔습니다."
    b = "님이 나갔습니다."
    id_record = defaultdict(str)

    for r in record:
        r = r.split(" ")
        if len(r) > 2:
            id_record[r[1]] = r[2]

    for r in record:
        r = r.split(" ")
        temp = ""
        if r[0] == "Change":
            continue
        elif r[0] == "Enter":
            temp = id_record[r[1]] + a
        elif r[0] == "Leave":
            temp = id_record[r[1]] + b
        answer.append(temp)

    return answer