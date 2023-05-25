# programmers - 2022 kakao blind recruitment - k진수에서 소수개수 구하기
# https://school.programmers.co.kr/learn/courses/30/lessons/92335

def solution(n, k):
    answer = 0
    change = ""

    # 진수 변경
    for i in range(13, -1, -1):
        re = n // (k ** i)
        change += str(re)
        n = n % (k ** i)

    lst = change.split("0")

    # 소수 찾기
    for num in lst:
        if num != '':
            number = int(num)
            if number == 1:
                continue
            if number == 2 or number == 3:
                answer += 1
                continue
            fin = int(number ** (1/2))
            for r in range(2, fin + 1):
                if number % r == 0:
                    break
            else:
                answer += 1
    return answer