def solution(wallpaper):
    answer = []
    min_i = 50
    min_j = 50
    max_i = 0
    max_j = 0
    for i in range(len(wallpaper)):
        for j in range(len(wallpaper[0])):
            if wallpaper[i][j] == "#":
                min_i = min(min_i, i)
                min_j = min(min_j, j)
                max_i = max(max_i, i)
                max_j = max(max_j, j)
    answer.append(min_i)
    answer.append(min_j)
    answer.append(max_i+1)
    answer.append(max_j+1)
    return answer