def solution(answers):
    answer = []
    score = [0, 0, 0]
    chk = [[1, 2, 3, 4, 5],
          [2, 1, 2, 3, 2, 4, 2, 5],
          [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]
    len_chk = [5, 8, 10]
    i = 0
    n = len(answers)
    while i < n:
        for j in range(3):
            if answers[i] == chk[j][(i%len_chk[j])]:
                score [j] += 1
        i += 1
    for j in range(3):
        if score[j] == max(score):
            answer.append(j + 1)
    return answer