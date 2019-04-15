def R():
    cnt = [0] * 10



def C():

r, c, k = map(int, input().split())
r -= 1
c -= 1
A = [list(map(int, input().split())) for _ in range(3)]
row = 3
col = 3
while A[r][c] != k:
    if row >= col:
        R()
    else:
        C()