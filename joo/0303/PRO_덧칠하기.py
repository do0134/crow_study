# programmers 연습문제 - 덧칠하기
# https://school.programmers.co.kr/learn/courses/30/lessons/161989

def solution(n, m, section):
    answer = 0
    maxx = 0
    for num in section:
        if num > maxx:
            answer += 1
            maxx = num + m - 1
    return answer


n1, m1 = 8, 4
s1 = [2, 3, 6]
n2, m2 = 5, 4
s2 = [1, 3]
n3, m3 = 4, 1
s3 = [1, 2, 3, 4]
print(solution(n1, m1, s1))
print(solution(n2, m2, s2))
print(solution(n3, m3, s3))
