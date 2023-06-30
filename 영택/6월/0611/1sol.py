# 백준 15059 Hard Choice
# https://www.acmicpc.net/problem/15059

ready = list(map(int,input().split()))
order = list(map(int,input().split()))
answer = 0

for i in range(3) :
    if ready[i] < order[i] :
        answer += order[i] - ready[i]

print(answer)