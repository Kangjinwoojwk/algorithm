for tc in range(1, int(input()) + 1):
    N, M, K, A, B = map(int, input().split())
    a = map(int, input().split())
    b = map(int, input().split())
    t = map(int, input().split())
    customer = [True for _ in range(K)]
    customerRecord = [[0, 0]for _ in range(K)]
    ado = [0 for _ in a]
    bdo = [0 for _ in b]
    while True not in customer:
