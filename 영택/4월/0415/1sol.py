# 프로그래머스 바탕화면 정리
# https://school.programmers.co.kr/learn/courses/30/lessons/161990

def solution(wallpaper):
    lx = ly = int(1e9)
    rx = ry = -1
    for i in range(len(wallpaper)):
        for j in range(len(wallpaper[i])):
            if wallpaper[i][j] == "#":
                lx = min(lx, i)
                ly = min(ly, j)
                rx = max(rx, i)
                ry = max(ry, j)

    return [lx, ly, rx + 1, ry + 1]