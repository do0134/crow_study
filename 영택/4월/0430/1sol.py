# 백준 1655 가운데를 말해요
# https://www.acmicpc.net/problem/1655

import heapq as h
import sys
n = int(input())
heap1 = list()
heap2 = list()
h1 = h2 = 0
for i in range(n) :
    value = int(sys.stdin.readline())
    if not h1 :
        h.heappush(heap1, -value)
        h1 += 1
    elif not h2 :
        if -heap1[0] > value :
            temp = h.heappop(heap1)
            h.heappush(heap1, -value)
            h.heappush(heap2, -temp)
        else :
            h.heappush(heap2, value)
        h2 += 1
    elif -heap1[0] >= value :
        h.heappush(heap1, -value)
        h1 += 1
    elif heap2[0] <= value :
        h.heappush(heap2, value)
        h2 += 1
    elif -heap1[0] < value < heap2[0] :
        if h1 <= h2 :
            h.heappush(heap1,-value)
            h1 += 1
        else :
            h.heappush(heap2,value)
            h2 += 1
    if not (h1+h2)%2 :
        if h1 > h2 :
            while h1 != h2 :
                temp = -h.heappop(heap1)
                h1 -= 1
                h.heappush(heap2, temp)
                h2 += 1
        elif h1 < h2 :
            while h1 != h2 :
                temp = h.heappop(heap2)
                h2 -= 1
                h.heappush(heap1, -temp)
                h1 += 1
    elif h1 > h2+1  :
        while h1 != h2+1 and h1 != h2 :
            temp = -h.heappop(heap1)
            h1 -= 1
            h.heappush(heap2, temp)
            h2 += 1
    elif h1 < h2+1  :
        while h1 != h2+1 :
            temp = h.heappop(heap2)
            h2 -= 1
            h.heappush(heap1, -temp)
            h1 += 1
    print(-heap1[0])




