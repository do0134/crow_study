# 백준 1182 부분수열의 합
# https://www.acmicpc.net/problem/1182

from itertools import combinations

n,s = map(int,input().split())
arr = list(map(int,input().split()))
answer = 0

for i in range(1,n+1) :
    for combination in combinations(arr,i) :
        if sum(combination) == s :
            answer += 1

print(answer)
