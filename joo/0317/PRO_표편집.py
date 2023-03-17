# 이게 내가 예전에 풀었던 코드. 정확성은 100인데 효율성이 0점이다
# 다시 풀어보려고 들고왔음

# def solution(n, k, cmd):
#     answer = ''
#     now = k
#     deleted = []
#     resultList = [i for i in range(n)]
#     for comm in cmd:
#         if comm[0] == "D":
#             now += int(comm[2:])
#         elif comm[0] == "U":
#             now -= int(comm[2:])
#         elif comm[0] == "C":
#             drow = resultList.pop(now)
#             deleted.append((now, drow))
#             if now >= len(resultList):
#                 now = len(resultList) - 1
#         elif comm[0] == "Z":
#             zrow = deleted.pop()
#             resultList.insert(zrow[0], zrow[1])
#             if now >= zrow[0]:
#                 now += 1
#
#     for i in range(n):
#         for j in range(len(deleted)):
#             if deleted[j][1] == i:
#                 answer += "X"
#                 break
#         else:
#             answer += "O"
#     return answer


# 새로 짠 코드

# from collections import deque
#
# def solution(n, k, cmd):
#     answer = ''
#     table = [1 for _ in range(n)]
#     now = k
#     q = deque()
#     for comm in cmd:
#         alpha = comm[0]
#         if alpha == "U":
#             num = int(comm[2])
#             i = 1
#             while num > 0:
#                 if table[now - i] == 1:
#                     now -= i
#                     num -= 1
#                     i = 1
#                 else:
#                     i += 1
#         elif alpha == "D":
#             num = int(comm[2])
#             i = 1
#             while num > 0:
#                 if table[now + i] == 1:
#                     now += i
#                     num -= 1
#                     i = 1
#                 else:
#                     i += 1
#         elif alpha == "C":
#             table[now] = 0
#             q.append(now)
#             if now == n - 1:
#                 i = 1
#                 while 0 <= now - i < n:
#                     if table[now - i] == 1:
#                         now -= i
#                         break
#                     else:
#                         i += 1
#             else:
#                 i = 1
#                 while 0 <= now - i < n:
#                     if table[now + i] == 1:
#                         now += i
#                         break
#                     else:
#                         i += 1
#         else:
#             table[q.pop()] = 1
#
#     for n in table:
#         if n == 1:
#             answer += 'O'
#         else:
#             answer += 'X'
#     return answer


# 정확성 2 케이스, 효율성 1케이스 실패,, 진짜 조금 틀린 것 같은데 그게 어딜까..
from collections import deque


def solution(n, k, cmd):
    answer = ''
    table = [1 for _ in range(n)]
    idxs = [[i - 1, i + 1] for i in range(n)]
    idxs[0][0] = 0
    idxs[n - 1][1] = n - 1
    now = k
    q = deque()
    for comm in cmd:
        alpha = comm[0]
        if alpha == "U":
            num = int(comm[2:])
            for _ in range(num):
                now = idxs[now][0]
        elif alpha == "D":
            num = int(comm[2:])
            for _ in range(num):
                now = idxs[now][1]
        elif alpha == "C":
            table[now] = 0
            q.append(now)
            if now != 0:
                idxs[idxs[now][0]][1] = idxs[now][1]
            if now != n - 1:
                idxs[idxs[now][1]][0] = idxs[now][0]
            if now == n - 1:
                now = idxs[now][0]
            else:
                now = idxs[now][1]
        else:
            deleted = q.pop()
            table[deleted] = 1
            if deleted != 0:
                idxs[idxs[deleted][0]][1] = deleted
            if deleted != n - 1:
                idxs[idxs[deleted][1]][0] = deleted

    for n in table:
        if n == 1:
            answer += 'O'
        else:
            answer += 'X'
    return answer


n1, k1 = 8, 2
c1 = ["D 2", "C", "U 3", "C", "D 4", "C", "U 2", "Z", "Z"]
c2 = ["D 2", "C", "U 3", "C", "D 4", "C", "U 2", "Z", "Z", "U 1", "C"]
print(solution(n1, k1, c1))
