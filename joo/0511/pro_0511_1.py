def solution(cap, n, deliveries, pickups):
    answer = 0
    deliveries = deliveries[::-1]
    pickups = pickups[::-1]
    deli = 0
    pick = 0
    for i in range(n):
        deli += deliveries[i]
        pick += pickups[i]

        while deli > 0 or pick > 0:
            deli -= cap
            pick -= cap
            answer += (n - i) * 2

    return answer