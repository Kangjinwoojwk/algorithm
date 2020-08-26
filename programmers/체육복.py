def solution(n, lost, reserve):
    answer = 0
    reserve.sort()
    judge = [1] * n
    for i in lost:
        judge[i - 1] -= 1
    for i in reserve :
        judge[i - 1] += 1
    i = 0
    while i < n:
        if judge[i] == 2:
            if i-1 >= 0 and judge[i - 1] == 0:
                judge[i - 1] += 1
                judge[i] -= 1
            elif i + 1 < n and judge[i + 1] == 0:
                judge[i + 1] += 1
                judge[i] -= 1
        i += 1
    for i in judge:
        if i != 0:
            answer += 1
    return answer