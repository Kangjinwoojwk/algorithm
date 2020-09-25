def solution(N, number):
    result = [{int(str(N) * i)} for i in range(1, 9)]
    if N == number:
        return 1
    for i in range(1, 8):
        for j in range(i):
            for a in result[j]:
                for b in result[i - j - 1]:
                    result[i].add(a + b)
                    if a > b:
                        result[i].add(a - b)
                    result[i].add(a * b)
                    if b != 0:
                        result[i].add(a // b)
        if number in result[i]:
            return i + 1
    return -1