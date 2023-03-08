# programmers 2022 kakao blind recruitment - 양과 늑대
# https://school.programmers.co.kr/learn/courses/30/lessons/92343

def dfs(cur, visited, sheep, wolf, k, dic, info, track):
    switch = False
    if info[cur] == 0 and cur not in track:
        sheep += 1
        visited = {cur: True}
        k.append(sheep)
        track.append(cur)
        switch = True
    if info[cur] == 1 and cur not in track:
        wolf += 1
        track.append(cur)
        switch = True
    if sheep == wolf:
        del visited[cur]
        if switch == True:
            track.pop()
        return
    for node in dic[cur]:
        if node not in visited:
            visited[node] = True
            dfs(node, visited, sheep, wolf, k, dic, info, track)
    del visited[cur]
    if switch == True:
        track.pop()


def solution(info, edges):
    dic = dict()
    k = []
    for i in edges:
        x = i[0]
        y = i[1]
        if x not in dic:
            dic[x] = [y]
        else:
            dic[x].append(y)
        if y not in dic:
            dic[y] = [x]
        else:
            dic[y].append(x)
    visited = {}
    track = []
    dfs(0, visited, 0, 0, k, dic, info, track)
    k.sort(reverse=True)
    answer = k[0]
    return answer


i1 = [0, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1]
e1 = [[0, 1], [1, 2], [1, 4], [0, 8], [8, 7], [9, 10], [9, 11], [4, 3], [6, 5], [4, 6], [8, 9]]
print(solution(i1, e1))
