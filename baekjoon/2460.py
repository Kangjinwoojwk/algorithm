ans = 0
people = 0
for _ in range(10):
    people_out, people_in = map(int, input().split())
    people -= people_out
    people += people_in
    if people > ans:
        ans = people
print(ans)