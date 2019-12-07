def solution(A):
    # write your code in Python 3.6
    data = [0] * len(A)
    j = 1
    for i in A:
        data[i - 1] = j
        j += 1
    temp = 0
    answer = 0
    for i in data:
        if i > temp:
            answer += 1
            temp = i
    return answer

print(solution([1, 3, 4, 2, 5]))
