# 프로그래머스 모음사전
# https://school.programmers.co.kr/learn/courses/30/lessons/84512
def solution(word):
    d = set()

    def dfs(idx,w) :
        nonlocal d
        if idx == 5 :
            return
        for i in ("A", "E", "I", "O", "U") :
            temp = w+i
            d.add(temp)
            dfs(idx+1,temp)

    dfs(0,"")
    d = sorted(list(d))
    answer = d.index(word)+1

    return answer