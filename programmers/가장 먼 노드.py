def solution(n, edge):
    answer = 0
    relation = [list() for _ in range(n + 1)]
    distance = [n + 1] * (n + 1)
    for i in edge:
        relation[i[0]].append(i[1])
        relation[i[1]].append(i[0])
    st = [1]
    step = 0
    while st:
        for _ in range(len(st)):
            temp = st.pop(0)
            if distance[temp] == n + 1:
                distance[temp] = step
                st += relation[temp]
        step += 1
    for i in range(n + 1):
        if distance[i] == n + 1:
            distance[i] = 0
    answer = distance.count(max(distance))
    return answer