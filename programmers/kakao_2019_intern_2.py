def solution(s):
    answer = []
    s = s[2:-2]
    s = s.split('},{')
    s.sort(key = lambda x : len(x))
    s = [list(map(int, i.split(','))) for i in s]
    for i in s:
        for j in i:
            if j not in answer:
                answer.append(j)
    return answer