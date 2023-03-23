def solution(key, lock):
    answer = True
    key_idxs = []
    lock_idxs = []
    # 열쇠 돌기 찾기
    for i in range(len(k1)):
        for j in range(len(k1)):
            if key[i][j]:
                key_idxs.append([i, j])

    # 자물쇠 홈 찾기
    for i in range(len(l1)):
        for j in range(len(l1)):
            if not lock[i][j]:
                lock_idxs.append([i, j])
    print(key_idxs, lock_idxs)

    def clockwise(x, y, w):
        return [y, abs(x - (w - 1))]

    def counterclockwise(x, y, w):
        return [abs(y - (w - 1)), x]

    def BFS(keys, locks, N):
        flag = 0
        for x, y in keys:
            if x < 0 or x >= N or y < 0 or y >= N:
                flag = 1

        return flag
    return answer


k1 = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
l1 = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
print(solution(k1, l1))
