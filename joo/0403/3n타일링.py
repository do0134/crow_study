# programmers 연습문제 - 3 X n 타일링
# https://school.programmers.co.kr/learn/courses/30/lessons/12902
def solution(n):
    mod = 1000000007
    dp = [0 for _ in range(n+1)]
    dp[2] = 3
    if n > 2:
        dp[4] = 11
        for i in range(6, n+1, 2):
            dp[i] = dp[i-2] * 3 + 2
            for j in range(i-4, -1, -2):
                dp[i] += dp[j] * 2
            dp[i] %= mod

    return dp[n]


n1 = 4
print(solution(n1))