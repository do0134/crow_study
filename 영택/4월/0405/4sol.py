# 프로그래머스 카펫
# https://school.programmers.co.kr/learn/courses/30/lessons/42842

def solution(brown, yellow):
    size = brown+yellow
    for i in range(3,size//3+1) :
        a = i
        b = size // a
        if brown == a*2 + b*2 - 4 and yellow == a*b-brown:
            return sorted([a,b], reverse = True)