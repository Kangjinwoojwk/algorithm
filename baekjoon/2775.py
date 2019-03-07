T = int(input())
apt = [[i for i in range(0, 15)]]
for i in range(1, 15):
    apt.append([sum(apt[i - 1][:j + 1]) for j in range(0, 15)])
for _ in range(T):
    k = int(input())
    n = int(input())
    print(apt[k][n])