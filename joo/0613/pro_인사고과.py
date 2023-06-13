# programmers 연습문제 - 인사고과
# https://school.programmers.co.kr/learn/courses/30/lessons/152995

def solution(scores):
    answer = 0
    members = []
    #     # 모든 사원의 점수를 비교해서 둘 다 낮은 점수를 가진 사원은 빼기
    #     for i in range(len(scores)):
    #         now = scores[i][0] + scores[i][1]
    #         for j in range(len(scores)):
    #             if i == j:
    #                 continue
    #             if now >= scores[j][0] + scores[j][1]:
    #                 continue
    #             if scores[i][0] < scores[j][0] and scores[i][1] < scores[j][1]:
    #                 break
    #         else:
    #             members.append(i)
    #         if i == 0 and len(members) == 0:
    #             answer = -1
    #             break

    #     # 합으로 등수 매기기
    #     if len(members) != 0:
    #         wonho = scores[0][0] + scores[0][1]
    #         for mi in members:
    #             if wonho < scores[mi][0] + scores[mi][1]:
    #                 answer += 1

    wonho = scores[0]
    scores.sort(key=lambda x: -(x[0] + x[1]))
    here = 0
    for i in range(len(scores)):
        if scores[i] == wonho:
            here = i
            break
    scores = scores[:here + 1]
    for i in range(len(scores)):
        for j in range(i):
            if scores[i][0] < scores[j][0] and scores[i][1] < scores[j][1]:
                if wonho == scores[i]:
                    answer = -1
                break
        else:
            answer += 1
        if answer == -1:
            break

    return answer