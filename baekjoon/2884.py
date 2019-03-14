hour, minute = map(int, input().split())
time = hour * 60 + minute - 45
time %= (24 * 60)
hour = time // 60
minute = time % 60
print(hour, minute)