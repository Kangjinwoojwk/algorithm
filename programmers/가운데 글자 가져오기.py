def solution(s):
    answer = s
    while len(answer) > 2:
        answer = answer[1:-1]
    return answer