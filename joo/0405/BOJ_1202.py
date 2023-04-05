# BOJ 1202 보석 도둑
# https://www.acmicpc.net/problem/1202
import heapq
import sys

N, K = map(int, sys.stdin.readline().split())
jewel = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
weight = [int(sys.stdin.readline()) for _ in range(K)]
weight.sort()
jewel.sort()
result = 0
tmp = []

for weight in weight:
    while jewel and jewel[0][0] <= weight:
        heapq.heappush(tmp, -jewel[0][1])
        heapq.heappop(jewel)
    if tmp:
        result -= heapq.heappop(tmp)
print(result)
