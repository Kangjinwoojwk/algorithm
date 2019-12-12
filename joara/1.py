data = [list(input().split()) for i in range(n)]
food = {data[0][i]: [data[j][i]for j in range(1, len(data))] for i in range(1, len(data[0]))}
friend = [False] * (len(data) - 1)
visit = [True] * len(food)
def sol(start, n):
    if n == 0:

        else:
            return True
    for i in range(start, len(food)):
        if visit[i]:
            visit[i] = False
            temp = sol(start + 1, n - 1)
            if temp:
                return temp
            visit[i] = True
    return False

