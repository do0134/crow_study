from collections import defaultdict


def L(target, cnt):
    direction = ["N", "W", "S", "E"]
    now = direction.index(robot[target][2])
    cnt %= 4
    now += cnt
    if now >= 4:
        now = 4 - now
    robot[target][2] = direction[now]



def R(target, cnt):
    direction = ["N", "E", "S", "W"]
    now = direction.index(robot[target][2])
    cnt %= 4
    now += cnt
    if now >= 4:
        now = 4 - now
    robot[target][2] = direction[now]



def F(target, cnt):
    cr, cc, drc = robot[target]
    arr[cr][cc] = 0
    for i in range(1, cnt+1):
        if drc == "N":
            nr, nc = cr-i, cc
        elif drc == "W":
            nr, nc = cr, cc-i
        elif drc == "S":
            nr, nc = cr+i, cc
        elif drc == "E":
            nr, nc = cr, cc+i
        if 0 <= nr < b and 0 <= nc < a:
            if not arr[nr][nc]:
                pass
            else:
                return f"Robot {target} crashes into robot {arr[nr][nc]}"

        else:
            return f"Robot {target} crashes into the wall"

    else:
        robot[target] = [nr, nc, drc]
        arr[nr][nc] = target
    return ""


a, b = map(int,input().split())
n, m = map(int,input().split())
arr = [[0]*a for _ in range(b)]
robot = defaultdict(list)
answer = ""
for i in range(1, n+1):
    c, r, d = input().split()
    c, r = int(c) - 1, b - int(r)
    robot[i] = [r, c, d]
    arr[r][c] = i

for _ in range(m) :
    x, y, z = input().split()
    x, z = int(x), int(z)
    if y == "L":
        L(x, z)
    elif y == "R":
        R(x, z)
    else:
        answer = F(x, z)
        if answer:
            break
if not answer:
    answer = "OK"
print(answer)
