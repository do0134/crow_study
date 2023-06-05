# programmers - 연속된 부분 수열의 합
# https://school.programmers.co.kr/learn/courses/30/lessons/178870


def solution(sequence, k):
    answer = []
    if k in sequence:
        return [sequence.index(k), sequence.index(k)]
    l = 0
    r = 0
    n = len(sequence)
    temp = 0
    s = len(sequence)
    while r < n:
        temp += sequence[r]
        r += 1
        if temp > k:
            while temp > k:
                temp -= sequence[l]
                l += 1
        if temp == k:
            if s > (r - l - 1):
                s = (r - l - 1)
                answer = [l, r - 1]

    return answer
