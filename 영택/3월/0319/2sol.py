# 프로그래머스 스킬체크 레벨 2

def bfs(p) :
    q = list()
    for i in range(5) :
        for j in range(5) :
            if p[i][j] == "P" :
                q.append((i,j))
    for i in range(len(q)) :
        for j in range(i+1,len(q)) :
            cr,cc= q[i]
            nr,nc = q[j]
            check = abs(cr-nr) + abs(cc-nc)
            if check > 2 :
                continue
            if cc == nc :
                for k in range(cr+1,nr) :
                    if p[k][cc] == "X" :
                        break
                else :
                    return 0
            elif cr == nr :
                for k in range(cc+1,nc) :
                    if p[nr][k] == "X" :
                        break
                else :
                    return 0
            else :
                if p[nr][cc] == "X" and p[cr][nc] == "X" :
                    break
                else :
                    return 0
    return 1







def solution(places):
    answer = []
    cnt = 0
    for place in places :
        cnt += 1
        # print(cnt)
        answer.append(bfs(place))
    return answer