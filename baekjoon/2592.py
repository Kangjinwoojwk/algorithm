data = dict()
max_count = 1
for _ in range(10):
    get_data = int(input())
    if get_data in data:
        data[get_data] += 1
        if data[get_data] > max_count:
            max_count = data[get_data]
    else:
        data[get_data] = 1
print(int(sum([k * v for k, v in data.items()])/10))
for k, v in data.items():
    if v == max_count:
        print(k)
        exit()