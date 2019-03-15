li = [sum(map(int, input().split())) for _ in range(5)]
a = max(li)
for i in range(5):
    if li[i] == a:
        print(i + 1, a)
        break