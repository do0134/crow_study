# 프로그래머스 단어 변환
# https://school.programmers.co.kr/learn/courses/30/lessons/43163

def back_tracking(word, target, v, cnt, words) :
    global answer
    if word == target :
        answer = min(answer, cnt)
        return
    for i in words :
        if i not in v and check(i, word) == 1 :
            back_tracking(i,target,v+[i],cnt+1,words)

def check(target, origin) :
    diff = 0
    for i in range(len(target)) :
        if target[i] != origin[i] :
            diff += 1
    return diff

def solution(begin, target, words):
    global answer
    answer = int(1e9)
    back_tracking(begin,target, [], 0, words)
    if answer == int(1e9) :
        return 0
    return answer