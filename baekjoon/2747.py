def fi(n):
    if n < len(fibo):
        return fibo[n]
    else:
        fibo.append(fi(n - 1) + fi(n - 2))
        return fibo[n]
fibo = [0, 1, 1]
print(fi(int(input())))