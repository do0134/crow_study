from collections import deque

# 백준 1697 숨바꼭질
# https://www.acmicpc.net/problem/1697


n, k = map(int,input().split())
m = max(n,k)
v = [int(1e9)]*(2*m+1)
q = deque()
q.append(n)
v[n] = 0
while q:
    cr = q.popleft()
    first = cr - 1
    second = cr + 1
    third = cr*2
    if 0 <= first < 2*m+1 and v[first] > v[cr] + 1:
        q.append(first)
        v[first] = v[cr] + 1
    if 0 <= second < 2*m+1 and v[second] > v[cr] + 1:
        q.append(second)
        v[second] = v[cr] + 1
    if 0 <= third < 2*m+1 and v[third] > v[cr] + 1:
        q.append(third)
        v[third] = v[cr] + 1

print(v[k])
