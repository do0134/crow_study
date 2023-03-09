# 백준 소트 게임
# https://www.acmicpc.net/problem/1327

from collections import deque, defaultdict
from copy import deepcopy
n,k = map(int,input().split())
arr = list(map(int,input().split()))

def bfs() :
    target = sorted(arr)
    q = deque()
    q.append(arr)
    cnt = -1
    v = defaultdict(int)
    v[str(arr)] = 1
    while len(q) != 0 :
        cn = len(q)
        cnt += 1
        for _ in range(cn) :
            c_arr = q.popleft()

            if c_arr == target :
                return cnt

            for i in range(n-k+1) :
                temp = list()
                for j in range(i+k-1,i-1,-1) :
                    temp.append(c_arr[j])
                t_arr = deepcopy(c_arr)
                for p in range(k) :
                    t_arr[i+p] = temp[p]
                if not v[str(t_arr)] :
                    v[str(t_arr)] = 1
                    q.append(t_arr)

    return -1


print(bfs())
