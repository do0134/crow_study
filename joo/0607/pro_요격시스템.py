def solution(targets):
    answer = 1
    targets.sort()
    end = targets[0][1]
    for s, e in targets[1:]:
        if s >= end:
            answer += 1
            end = e
        elif e <= end:
            end = e
    return answer