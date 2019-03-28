a, b, c = map(int, input().split())
d = a * 3600 + b * 60 + c + int(input())
d %= 86400
a = d // 3600
d %= 3600
b = d // 60
d %= 60
print(a, b, d)
