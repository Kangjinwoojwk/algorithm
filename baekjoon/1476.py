E, S, M = map(int, input().split())
while True:
    if E == S == M:
        break
    if E <= S and E <= M:
        E += 15
    elif S <= E and S <= M:
        S += 28
    elif M <= E and M <= S:
        M += 19
print(E)