# 프로그래머스 성격유형 검사하기
# https://school.programmers.co.kr/learn/courses/30/lessons/118666

def solution(survey, choices):
    mbti = "RTCFJMAN"
    mbti_dict = {i: 0 for i in mbti}
    for i, j in zip(survey, choices):
        if j == 1:
            mbti_dict[i[0]] += 3
        elif j == 2:
            mbti_dict[i[0]] += 2
        elif j == 3:
            mbti_dict[i[0]] += 1
        elif j == 5:
            mbti_dict[i[1]] += 1
        elif j == 6:
            mbti_dict[i[1]] += 2
        elif j == 7:
            mbti_dict[i[1]] += 3
    answer = ''
    if mbti_dict["R"] >= mbti_dict["T"]:
        answer += "R"
    else:
        answer += "T"
    if mbti_dict["C"] >= mbti_dict["F"]:
        answer += "C"
    else:
        answer += "F"
    if mbti_dict["J"] >= mbti_dict["M"]:
        answer += "J"
    else:
        answer += "M"
    if mbti_dict["A"] >= mbti_dict["N"]:
        answer += "A"
    else:
        answer += "N"

    return answer