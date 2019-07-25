for tc in range(int(input())):
    N = int(input())
    data = [input() for _ in range(N)]
    data = list(set(data))
    data.sort()
    data = [(len(data[i]), data[i]) for i in range(len(data))]
    data.sort()
    data = [i[1] for i in data]
    print('#{}'.format(tc + 1))
    for i in data:
        print(i)