for tc in range(int(input())):
    N = int(input())
    data = list(map(int, input().split()))
    print((max(data) - min(data)) * 2)