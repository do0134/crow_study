# 백준 13335 트럭
# https://www.acmicpc.net/problem/13335

from collections import deque

n, w, l = map(int,input().split())
truck = deque(list(map(int,input().split())))
bridge = deque()

time = 0
weight = 0

while truck :
    if not bridge :
        bridge.append([truck.popleft(),1])
        time += 1
        weight += bridge[-1][0]
    elif weight+truck[0] > l :
        t_temp = w-bridge[0][1]+1
        time += t_temp
        temp = bridge.popleft()
        for b in bridge :
            b[1] += t_temp
        weight -= temp[0]
        if weight + truck[0] <= l :
            bridge.append([truck.popleft(),1])
            weight += bridge[-1][0]
    elif weight+truck[0] <= l :
        for b in bridge :
            b[1] += 1
        if bridge[0][1] > w :
            temp = bridge.popleft()
            weight -= temp[0]
        time += 1
        bridge.append([truck.popleft(),1])
        weight += bridge[-1][0]

if bridge :
    time += w-bridge[-1][1]+1

print(time)