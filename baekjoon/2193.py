li = [0, 1, 1]
def sol(n):
    if n < len(li):
        return li[n]
    else:
        li.append(sol(n - 1) + sol(n - 2))
        return li[n]
N = int(input())
print(sol(N))
