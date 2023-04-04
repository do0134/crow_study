# 백준 - 15684 (한화 기출이랑 비슷하다고 해서 풀이)
# https://www.acmicpc.net/problem/15684

# i -> i 확인
def check():
    for j in range(N):
        tmp = j
        for i in range(H):
            if table[i][tmp]:
                tmp += 1
            elif tmp > 0 and table[i][tmp-1]:
                tmp -= 1
        if tmp != j:
            return False
    return True


def DFS(x, y, cnt):
    global ans
    # 가지치기; cnt가 최솟값보다 크면 return
    if cnt >= ans:
        return
    # i -> i 가는지 확인
    if check():
        ans = min(ans, cnt)
        return
    # 가지치기; cnt == 3이면 return
    if cnt == 3:
        return
    # 사다리 가로줄 넣어주기
    for i in range(x, H):
        # i가 x 와 같으면 즉, 시작한 세로 좌표와 같으면 해당 좌표부터 시작, 다르면 0부터 시작
        k = y if i == x else 0
        for j in range(k, N-1):
            if not table[i][j]:
                table[i][j] = 1
                DFS(i, j+2, cnt + 1)
                table[i][j] = 0


N, M, H = map(int, input().split())
table = [[0] * N for i in range(H)]
for _ in range(M):
    a, b = map(int, input().split())
    table[a-1][b-1] = 1

ans = 4
DFS(0, 0, 0)
print(ans if ans < 4 else -1)


