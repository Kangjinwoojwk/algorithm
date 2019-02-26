test = input()
num_cnt = [test.count(str(i)) for i in range(10)]
Max_without = 0
for idx, i in enumerate(num_cnt):
    if idx != 6 and idx != 9:
        if i > Max_without:
            Max_without = i
if 2 * Max_without >= num_cnt[6] + num_cnt[9]:
    print(Max_without)
else:
    if (num_cnt[6] + num_cnt[9]) % 2:
        print((num_cnt[6] + num_cnt[9] + 1) // 2)
    else:
        print((num_cnt[6] + num_cnt[9]) // 2)
