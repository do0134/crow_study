def solution(k, d):
    answer, d_pow = 0, d**2
    for i in range(0, d+1, k):
        answer += int((d_pow - i ** 2) ** .5) // k + 1
    return answer


k1 = 1
d1 = 5
print(solution(k1, d1))