# codetree - 샘의 피자학교
# https://www.codetree.ai/training-field/frequent-problems/sam-pizza-school/description?page=3&pageSize=20&username=

def push(t, start_i, start_j, end_i, end_j):
    dd = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    tmp_table = [[0] * end_j for _ in range(end_i)]
    for i in range(start_i, end_i):
        for j in range(start_j + 1, end_j):
            if t[i][j]:
                value = t[i][j]
                for dx, dy in dd:
                    nx, ny = i + dx, j + dy
                    if start_i <= nx < end_i and start_j <= ny < end_j and t[nx][ny]:
                        if t[i][j] > t[nx][ny]:
                            value -= (abs(t[i][j] - t[nx][ny]) // 5)
                        else:
                            value += (abs(t[i][j] - t[nx][ny]) // 5)
                tmp_table[i][j] = value
    t = tmp_table
    # print(*t, sep='\n')
    tmp_arr = []
    for j in range(start_j, end_j):
        for i in range(end_i - 1, -1, -1):
            if t[i][j]:
                tmp_arr.append(t[i][j])
            else:
                break
    return tmp_arr


n, k = map(int, input().split())
arr = list(map(int, input().split()))
table = [[0] * n for _ in range(n)]
cnt = 0

while True:
    # 가장 작은 위치에 밀가루 + 1
    minn = 3001
    minn_idx = []
    for i in range(n):
        if arr[i] == minn:
            minn_idx.append(i)
        elif arr[i] < minn:
            minn = arr[i]
            minn_idx = [i]
    for i in minn_idx:
        arr[i] += 1

    # 도우 말기
    table[n - 1] = arr
    now = past_now = 0
    now_dow = [[n - 1, 0]]
    minn_i = next_minn_i = n - 1
    while now < n:
        tmp = []
        minn_i = next_minn_i
        for x, y in now_dow:
            nx, ny = (n - 1) - (now - y + 1), now + 1 + (n - 1 - x)
            table[nx][ny] = table[x][y]
            table[x][y] = 0
            tmp.append([nx, ny])
            # if minn_i > x:
            #     minn_i = x
            if next_minn_i > nx:
                next_minn_i = nx
        past_now = now
        now += (n - 1 - minn_i + 1)
        # print(*table, sep="\n")
        if now + (n - 1 - next_minn_i + 1) >= n:
            break
        now_dow = tmp
        for j in range(past_now + 1, now + 1):
            now_dow.append([n - 1, j])

    # 도우 누르기 !
    arr = push(table, next_minn_i, past_now, n, n)

    # 도우 두번 반으로 접기
    tmp_fold = [[0] * n for _ in range(4)]
    # 1
    for j in range(n//2):
        tmp_fold[2][n//2+(n//2-j-1)] = arr[j]
    tmp_fold[3][n//2:] = arr[n//2:]
    # print("fold 1")
    # print(*tmp_fold, sep='\n')
    # print("2")
    # 2
    for i in range(2, 4):
        for j in range(n//2, n//2 + n//4):
            tmp_fold[3-i][n-1-j+(n//2)], tmp_fold[i][j] = tmp_fold[i][j], 0
    # print("fold 2")
    # print(*tmp_fold, sep='\n')


    # 도우 누르기
    # print("last push")
    arr = push(tmp_fold, 0, n//4, 4, n)
    # print(arr)
    maxx_chck = minn_chck = arr[0]
    for v in arr[1:]:
        if v > maxx_chck:
            maxx_chck = v
        elif v < minn_chck:
            minn_chck = v
    cnt += 1
    if maxx_chck - minn_chck <= k:
        break

print(cnt)