now = list(map(int, input().split(':')))
end = list(map(int, input().split(':')))
end[0] += 24
for i in range(3):
    end[i] -= now[i]
for i in range(2, 0, -1):
    if end[i] < 0:
        end[i - 1] -= 1
        end[i] += 60
end[0] %= 24
for i in range(3):
    if end[i] < 10:
        end[i] = '0' + str(end[i])
    else:
        end[i] = str(end[i])
print(':'.join(end))
