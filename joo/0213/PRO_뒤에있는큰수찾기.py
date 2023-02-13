# PROGRAMMERS - 연습문제 - 뒤에 있는 큰 수 찾기
# https://school.programmers.co.kr/learn/courses/30/lessons/154539

def solution(numbers):
    answer = [-1] * len(numbers)
    stack = []
    for i in range(len(numbers)):
        while stack and numbers[stack[-1]] < numbers[i]:
            answer[stack.pop()] = numbers[i]
        stack.append(i)
    return answer


n1 = [2, 3, 3, 5]
n2 = [9, 1, 5, 3, 6, 2]
print(solution(n2))
