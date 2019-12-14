def solution(a, b, budget):
    answer = 0
    for i in range(0, budget + 1, a):
        if (budget - i) % b == 0:
            answer += 1
    return answer