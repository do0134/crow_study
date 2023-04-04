# BOJ 17140 이차원 배열과 연산
# https://www.acmicpc.net/problem/17140

# 열 정렬
def csort(a):
    turn_table = list(map(list, zip(*reversed(a))))
    tmp = rsort(turn_table)
    tmp = list(map(list, zip(*reversed(tmp))))
    sorted_table = []
    for i in range(len(tmp)):
        sorted_table.append(tmp[i][::-1])
    return sorted_table


# 행 정렬
def rsort(a):
    sorted_table = []
    for i in range(len(a)):
        cnt = [[i, 0] for i in range(101)]
        sorted_r = []
        for j in range(len(a[0])):
            cnt[a[i][j]][1] += 1
        for j in range(1, 101):
            if cnt[j][1] != 0:
                sorted_r.append(cnt[j])
        sorted_r.sort(key=lambda x: (x[1], x[0]))
        tmp = []
        for j in range(len(sorted_r)):
            tmp.append(sorted_r[j][0])
            tmp.append(sorted_r[j][1])
        sorted_table.append(tmp)
    # 최대 길이에 맞춰 0 채워주기
    maxx = 0
    for i in range(len(sorted_table)):
        maxx = max(maxx, len(sorted_table[i]))
    for i in range(len(sorted_table)):
        for j in range(len(sorted_table[i]), maxx):
            sorted_table[i].append(0)
    return sorted_table


r, c, k = map(int, input().split())
arr = []
sec = 0
for _ in range(3):
    lst = list(map(int, input().split()))
    arr.append(lst)
if (0 <= r - 1 < len(arr) and 0 <= c - 1 < len(arr[0]) and arr[r - 1][c - 1] != k) or r - 1 > len(arr) or c - 1 > len(
        arr[0]):
    while sec <= 100:
        sec += 1
        if len(arr) >= len(arr[0]):
            arr = rsort(arr)
        else:
            arr = csort(arr)
        if 0 <= r - 1 < len(arr) and 0 <= c - 1 < len(arr[0]) and arr[r - 1][c - 1] == k:
            break

print(sec if sec <= 100 else -1)
