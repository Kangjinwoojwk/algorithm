# 정확도에선 안터졌다
from collections import deque
def solution(n, s, a, b, fares):
    answer = 1<<30
    edge = [[0] * (n + 1) for _ in range(n + 1)]
    for i in fares:
        edge[i[0]][i[1]] = i[2]
        edge[i[1]][i[0]] = i[2]
    queue = deque()
    queue.append([0, s])
    arrivea = list()
    arriveb = list()
    while queue:
        temp = queue.popleft()
        for i in range(n + 1):
            if edge[temp[-1]][i] and i not in temp[1:]:
                temp_temp = temp[:]
                temp_temp[0] += edge[temp[-1]][i]
                temp_temp.append(i)
                if i == a:
                    arrivea.append(temp_temp)
                if i == b:
                    arriveb.append(temp_temp)
                queue.append(temp_temp)
    for i in arrivea:
        if i[0] > answer:
            continue
        for j in arriveb:
            if j[0] > answer:
                continue
            sum_fare = i[0] + j[0]
            temp = list()
            for k in range(2, min(len(i), len(j))):
                if i[k] != j[k]:
                    temp = i[1:k]
                    break
            else:
                temp = i[1:k + 1]
            for k in range(len(temp) - 1):
                sum_fare -= edge[temp[k]][temp[k + 1]]
            if sum_fare < answer:
                answer = sum_fare
    return answer



# 효율성 체크 가기도 전에 시간이 터져 버린다
from collections import deque
def solution(n, s, a, b, fares):
    answer = 1 << 30
    edge = [[0] * (n + 1) for _ in range(n + 1)]
    for i in fares:
        edge[i[0]][i[1]] = i[2]
        edge[i[1]][i[0]] = i[2]
    queue = deque()
    queue.append([0, s])
    arrivea = list()
    arriveb = list()
    while queue:
        temp = queue.popleft()
        for i in range(n + 1):
            if edge[temp[-1]][i] and i not in temp[1:]:
                temp_temp = temp[:]
                temp_temp[0] += edge[temp[-1]][i]
                temp_temp.append(i)
                if i == a:
                    arrivea.append(temp_temp)
                if i == b:
                    arriveb.append(temp_temp)
                queue.append(temp_temp)
    for i in arrivea:
        for j in arriveb:
            sum_fare = i[0] + j[0]
            temp = list()
            for k in range(2, min(len(i), len(j))):
                if i[k] != j[k]:
                    temp = i[1:k]
                    break
            else:
                temp = i[1:k + 1]
            for k in range(len(temp) - 1):
                sum_fare -= edge[temp[k]][temp[k + 1]]
            if sum_fare < answer:
                answer = sum_fare
    return answer