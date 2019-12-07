# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A, B, C, D):
    # write your code in Python 3.6
    digit = [str(A), str(B), str(C), str(D)]
    visit = [True] * 4
    time = set()
    temp = str()
    for i in range(4):
        if visit[i]:
            temp += digit[i]
            visit[i] = False
            for j in range(4):
                if visit[j]:
                    temp += digit[j]
                    visit[j] = False
                    for k in range(4):
                        if visit[k]:
                            temp += digit[k]
                            visit[k] = False
                            for l in range(4):
                                if visit[l]:
                                    temp += digit[l]
                                    visit[l] = False
                                    time.add(temp)
                                    temp = temp[:-1]
                                    visit[l] = True
                            temp = temp[:-1]
                            visit[k] = True
                    temp = temp[:-1]
                    visit[j] = True
            temp = temp[:-1]
            visit[i] = True
    data = list()
    for i in time:
        if i[0] > '2':
            continue
        if i[0] == '2' and i[1] >= '4':
            continue
        if i[2] > '6':
            continue
        data.append(i)
    return len(data)

print(solution(6, 2, 4, 7))
