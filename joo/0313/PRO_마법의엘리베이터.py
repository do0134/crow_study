# programmers 연습문제 - 마법의 엘리베이터
# https://school.programmers.co.kr/learn/courses/30/lessons/148653

def solution(storey):
    answer = 0
    while storey > 5:
        now = storey % 10
        storey //= 10
        print(storey, now)
        if now > 5:
            magic = 10 - now
            storey += 1
        elif now == 5:
            magic = now
            if (storey % 10) >= 5:
                storey += 1
        else:
            magic = now
        print(magic)
        answer += magic
        print(answer)
    answer += storey
    return answer


s1 = 16
s2 = 2554
print(solution(646))
# 678 - 8 999 - 2 95 - 6