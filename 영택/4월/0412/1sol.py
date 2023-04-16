def dfs(idx, cnt, target, v):
    global name_list, answer, n
    if cnt >= answer:
        return
    if target == name_list:
        answer = min(cnt, answer)
        return

    l = r = 0
    while idx + l < n and v[idx + l] != 0:
        l += 1
    if idx + l >= n:
        pass
    else:
        v[idx + l] = 1
        target[idx + l] = name_list[idx + l]
        dfs(idx + l, cnt + l + min(ord(name_list[idx + l]) - ord("A"), ord("Z") - ord(name_list[idx + l]) + 1), target, v)
        v[idx + l] = 0
        target[idx + l] = "A"

    while idx - r >= -n and v[idx - r] != 0:
        r += 1
    print(idx,r,idx-r, cnt, target)
    if idx - r < -n:
        pass
    else:
        if idx-r >= 0 :
            new_idx = idx-r
        else :
            new_idx = n+(idx-r)
        v[idx - r] = 1
        target[idx - r] = name_list[idx - r]
        dfs(new_idx, cnt + r + min(ord(name_list[idx - r]) - ord("A"), ord("Z") - ord(name_list[idx - r]) + 1),
            target, v)
        v[idx - r] = 0
        target[idx - r] = "A"


def solution(name):
    global answer, n, name_list
    answer = int(1e9)
    n = len(name)
    name_list = list(name)
    v = [0] * n
    v[0] = 1
    for i in range(n):
        if name_list[i] == "A":
            v[i] = 1
    temp = list("A" * n)
    temp[0] = name[0]
    dfs(0, min(ord(name_list[0]) - ord("A"), ord("Z") - ord(name_list[0]) + 1), temp, v)
    return answer
print(solution("ABABAAAAABA"))
