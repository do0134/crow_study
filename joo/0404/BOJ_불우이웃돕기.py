# BOJ 1414 불우이웃 돕기
# https://www.acmicpc.net/problem/1414
import heapq


def change(s):
    if 'a' <= s <= 'z':
        return ord(s) - 96
    elif 'A' <= s <= 'Z':
        return ord(s) - 38
    else:
        return 0


total = 0
N = int(input())
lancable = [[] for _ in range(N)]
for i in range(N):
    lst = list(input().strip())
    for j in range(N):
        num = change(lst[j])
        lancable[i].append([num, j])
        lancable[j].append([num, i])
        total += num

# print(total)
heap = [[1, 0]]
cnt = 0
dasom = 0
visited = [0] * N
flag = 0
while heap:
    if cnt == N:
        flag = 1
        break
    w, s = heapq.heappop(heap)
    if not visited[s] and w != 0:
        visited[s] = 1
        cnt += 1
        dasom += w
        for i in lancable[s]:
            heapq.heappush(heap, i)

# dasom_lan = 0
# for c in dasom:
#     dasom_lan += change(c)
print(total - dasom + 1 if flag else -1)

