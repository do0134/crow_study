# 프로그래머스 주식가격
# https://school.programmers.co.kr/learn/courses/30/lessons/42584

def solution(prices):
    answer = list()

    for i in range(len(prices) - 1):
        temp = 0
        for j in range(i, len(prices) - 1):
            if prices[i] <= prices[j]:
                temp += 1
            else:
                break
        answer.append(temp)
    answer.append(0)
    return answer

# def solution(prices):
#     stack = []
#     answer = [0] * len(prices)
#     for i in range(len(prices)):
#         if stack != []:
#             while stack != [] and stack[-1][1] > prices[i]:
#                 past, _ = stack.pop()
#                 answer[past] = i - past
#         stack.append([i, prices[i]])
#     for i, s in stack:
#         answer[i] = len(prices) - 1 - i
#     return answer