# BOJ 3584 가까운 조상 찾기
# https://www.acmicpc.net/problem/3584

T = int(input())
for _ in range(T):
    ans = 0
    N = int(input())
    arr = [0 for _ in range(N + 1)]
    for _ in range(N-1):
        a, b = map(int, input(). split())
        arr[b] = a
    node1, node2 = map(int, input().split())
    parent1, parent2 = [], []
    # print(*arr, sep='\n')
    now = node1
    while True:
        if now == 0:
            break
        parent1.append(now)
        now = arr[now]
    now = node2
    while True:
        if now == 0:
            break
        parent2.append(now)
        now = arr[now]
    for x in parent1:
        if x in parent2:
            ans = x
            break
    print(ans)