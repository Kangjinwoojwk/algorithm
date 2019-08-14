for tc in range(int(input())):
    data = list(map(int, input().split()))
    data.sort()
    if data[3] - data[1] >=4:
        print('KIN')
    else:
        print(sum(data[1:4]))