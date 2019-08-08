ans = 0
for tc in range(int(input())):
    student, apple = map(int, input().split())
    ans += apple % student
print(ans)