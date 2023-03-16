from collections import defaultdict, deque

n = int(input())
tree = defaultdict(list)
dp = [[0,0] for _ in range(n+1)]
v = [0]*(n+1)
for _ in range(n-1) :
    u,v = map(int,input().split())
    tree[u].append(v)
    tree[v].append(u)

q = deque()
q.append(1)
v[1] = 1
while q :
    c_friend = q.popleft()
    for i in tree[c_friend] :
        if not v[i] :
            q.append(i)
        dp[c_friend][1] += min()
