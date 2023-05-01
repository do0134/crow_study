# 프로그래머스 공원산책
# https://school.programmers.co.kr/learn/courses/30/lessons/172928

def solution(park, routes):
    start = [-1, -1]
    for i in range(len(park)):
        for j in range(len(park[0])):
            if park[i][j] == "S":
                start = [i, j]
                break
        if start != [-1, -1]:
            break
    for route in routes:
        direction, far = route.split(" ")
        far = int(far)
        d = [0, 0]
        if direction == "E":
            d = [0, 1]
        elif direction == "S":
            d = [1, 0]
        elif direction == "W":
            d = [0, -1]
        elif direction == "N":
            d = [-1, 0]
        nr = d[0] * far + start[0]
        nc = d[1] * far + start[1]
        if 0 <= nr < len(park) and 0 <= nc < len(park[0]):
            flag = False
            dr = start[0]
            dc = start[1]
            while far > 0:
                dr += d[0]
                dc += d[1]
                if park[dr][dc] == "X":
                    flag = True
                    break
                far -= 1
            if not flag:
                start = [nr, nc]

    return start