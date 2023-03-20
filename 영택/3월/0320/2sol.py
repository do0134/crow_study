# 프로그래머스 표현 가능한 이진트리
import sys
sys.setrecursionlimit(10**6)


def solution(numbers):
    answer = []
    for num in numbers:
        if num <= 3:
            answer.append(1)
            continue
        else:
            val = bin(num)[2:]
            size = 1
            while size < len(val):
                size = (size + 1) * 2 - 1
            val = "0" * (size - len(val)) + val
            temp = dfs(0, len(val) - 1, val)
            if temp:
                answer.append(1)
            else:
                answer.append(0)
    return answer


def dfs(s, e, bin_num):
    if s == e:
        return bin_num[s]

    mid = (s + e) // 2
    l = dfs(s, mid - 1, bin_num)
    r = dfs(mid + 1, e, bin_num)

    if not l or (bin_num[mid] == "0" and l == "1"):
        return False

    if not r or (bin_num[mid] == "0" and r == "1"):
        return False

    if l == "0" and r == "0" and bin_num[mid] == "0":
        return "0"

    return "1"

