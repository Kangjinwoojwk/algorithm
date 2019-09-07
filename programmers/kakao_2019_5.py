def solution(n, build_frame):
    build = [[0] * (n + 1) for _ in range(n + 1)]
    for i in build_frame:
        x, y, a, b = i
        if b:
            if a == 0:
                if y == 0 or build[x][y - 1] or build_frame[x - 1][y] >= 100:
                    build[x][y] += 1
            elif a == 1:
                if build[x][y - 1] % 100 == 1 or build[x + 1][y - 1] % 100 or(build[x - 1][y] >= 100 and build[x + 1][y]):
                    build[x][y] += 100
        else:
            if a == 0:
                if build[x][y + 1] % 100 != 1 and build[x - 1][y + 1] % 100





    answer = [[]]

    return answer