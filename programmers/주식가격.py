

# 정확성 통과 효율성 전부 시간초과
def solution(prices):
    answer = []
    day_length = [0]*10001
    while prices:
        i = prices.pop()
        answer = [day_length[i]] + answer
        for j in range(i + 1):
            day_length[j] += 1
        for j in range(i + 1, 10001):
            day_length[j] = 1
    return answer