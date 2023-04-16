# 프로그래머스 다리를 지나는 트럭
# https://school.programmers.co.kr/learn/courses/30/lessons/42583

from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0
    idx = 0
    bridge = deque([0] * bridge_length)
    sum_v = 0
    while idx < len(truck_weights):
        answer += 1
        a = bridge.popleft()
        sum_v -= a
        if sum_v + truck_weights[idx] > weight:
            bridge.append(0)
        elif sum_v + truck_weights[idx] <= weight:
            bridge.append(truck_weights[idx])
            sum_v += truck_weights[idx]
            idx += 1

    while sum_v != 0:
        answer += 1
        sum_v -= bridge.popleft()
        bridge.append(0)

    return answer