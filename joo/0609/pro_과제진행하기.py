# programmers 연습문제 - 과제 진행하기
# https://school.programmers.co.kr/learn/courses/30/lessons/176962


def solution(plans):
    answer = []
    for plan in plans:
        h, m = map(int, plan[1].split(":"))
        time = h * 60 + m
        plan[1] = time
        plan[2] = int(plan[2])
    plans.sort(key=lambda x: x[1])
    stack = []
    for i in range(len(plans) - 1):
        next = plans[i + 1][1] - plans[i][1]
        # 중단하는 경우
        if next < plans[i][2]:
            plans[i][2] -= next
            stack.append(plans[i])
        # 시간이 남은 경우
        elif next > plans[i][2]:
            answer.append(plans[i][0])
            next -= plans[i][2]
            while next > 0 and len(stack) > 0:
                if stack[-1][2] <= next:
                    next -= stack[-1][2]
                    answer.append(stack.pop()[0])
                else:
                    stack[-1][2] -= next
                    next = 0
        # 딱 맞는 경우
        else:
            answer.append(plans[i][0])
    answer.append(plans[-1][0])
    for lst in stack[::-1]:
        answer.append(lst[0])

    return answer
