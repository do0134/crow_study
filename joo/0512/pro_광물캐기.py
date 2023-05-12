# programmers - 연습문제 - 광물캐기
# https://school.programmers.co.kr/learn/courses/30/lessons/172927


dias = {"diamond": 1, "iron": 1, "stone": 1}
irons = {"diamond": 5, "iron": 1, "stone": 1}
stones = {"diamond": 25, "iron": 5, "stone": 1}

def repeat(minerals, dia, iron, stone, now, tired):
    global answer
    if (dia == 0 and iron == 0 and stone == 0) or now >= len(minerals):
        answer = min(answer, tired)
        return

    # diamond
    if dia > 0:
        dia_tired = tired
        for i in range(5):
            if now + i >= len(minerals):
                break
            dia_tired += dias[minerals[now+i]]
        repeat(minerals, dia-1, iron, stone, now+5, dia_tired)

    # iron
    if iron > 0:
        iron_tired = tired
        for i in range(5):
            if now + i >= len(minerals):
                break
            iron_tired += irons[minerals[now+i]]
        repeat(minerals, dia, iron-1, stone, now+5, iron_tired)

    # stone
    if stone > 0:
        stone_tired = tired
        for i in range(5):
            if now + i >= len(minerals):
                break
            stone_tired += stones[minerals[now+i]]
        repeat(minerals, dia, iron, stone-1, now+5, stone_tired)

def solution(picks, minerals):
    global answer
    answer = 50*25 + 1
    repeat(minerals, picks[0], picks[1], picks[2], 0, 0)
    return answer