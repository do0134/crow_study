# programmers 연습문제 - 숫자 카드 나누기
# https://school.programmers.co.kr/learn/courses/30/lessons/135807

from math import gcd


def solution(arrayA, arrayB):
    def findGCD(array):
        GCD = 0
        for i in range(len(array)):
            GCD = gcd(GCD, array[i])
        return GCD

    def checkGCD(array, GCD):
        for i in range(len(array)):
            if array[i] % GCD == 0:
                return 0
        return GCD

    gcdA, gcdB = findGCD(arrayA), findGCD(arrayB)
    gcdA, gcdB = checkGCD(arrayB, gcdA), checkGCD(arrayA, gcdB)

    if not (gcdA or gcdB):
        return 0
    return max(gcdA, gcdB)


a1 = [10, 17]
b1 = [5, 20]
print(solution(a1, b1))