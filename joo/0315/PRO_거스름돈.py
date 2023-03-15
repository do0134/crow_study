# programmers 연습문제 - 거스름돈
# https://school.programmers.co.kr/learn/courses/30/lessons/12907

# 정확도 100 효율성 0 코드

# answer = 0
#
#
# def solution(n, money):
#     global answer
#
#     def finn(index, cur_value):
#         global answer
#         # 거슬러 줄 돈과 같으면 answer += 1
#         if cur_value == n:
#             answer += 1
#             return
#         # 거슬러 줄 돈 보다 크거나 index가 음수가 되면 되돌아가기
#         if cur_value > n or index < 0:
#             return
#         # 몫으로 for문 돌리기
#         max_cnt = (n - cur_value) // money[index]
#         for cnt in range(max_cnt, -1, -1):
#             finn(index - 1, cur_value + (money[index] * cnt))
#
#     finn(len(money) - 1, 0)
#     return answer


# 효율성이 0점이어서 다시 짠 코드
# 효율성이 빵점이라서 DP로 풀어야하나 생각이 들었다,,,,

def solution(n, money):
    dp = [0 for _ in range(n + 1)]
    dp[0] = 1
    for i in range(len(money)):
        for j in range(money[i], n + 1):
            dp[j] += dp[j - money[i]]
    return dp[n]


n1 = 5
m1 = [1, 2, 5]
m2 = [1, 2, 3, 5]
print(solution(n1, m1))
