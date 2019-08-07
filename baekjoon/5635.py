youngest_day = 0
youngest_name = ''
oldest_day = 99999999
oldest_name = ''
for tc in range(int(input())):
    name, day, month, year = input().split()
    day = int(day)
    month = int(month)
    year = int(year)
    date = year * 10000 + month * 100 + day
    if oldest_day > date:
        oldest_day = date
        oldest_name = name
    if youngest_day < date:
        youngest_day = date
        youngest_name = name
print(youngest_name)
print(oldest_name)