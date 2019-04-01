N = int(input())
score = {
    'A+': 4.3,
    'A0': 4.0,
    'A-': 3.7,
    'B+': 3.3,
    'B0': 3.0,
    'B-': 2.7,
    'C+': 2.3,
    'C0': 2.0,
    'C-': 1.7,
    'D+': 1.3,
    'D0': 1.0,
    'D-': 0.7,
    'F': 0.0
}
sum_value = 0
sum_hak = 0
for _ in range(N):
    li = input().split()
    li[1] = int(li[1])
    sum_hak += li[1]
    sum_value += li[1] * score[li[2]]
print(format(round((sum_value/sum_hak) + 0.001, 2), '.2f'))
