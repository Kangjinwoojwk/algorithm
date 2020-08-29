# 줄별로 사라지는 칸 수는 공식으로 나오니 이를 이용해서 답을 내는 코드
# 이 코드가 아니라고 한다. 왜지? 둘을 확인하는데 계속 같다고 나오는데...
def solution(w,h):
    answer = w * h
    if h > w:
        w, h = h, w
    chk = w // h
    if w % h:
        chk += 1
    answer -= chk * h
    return answer

# 공식적인 코드, 최소공배수를 이용한다.
import math
def solution1(w,h):
    return w*h - (w+h-math.gcd(w,h))


for i in range(1, 100000000):
    print(i)
    for j in range(1, 10000000):
        if solution(i, j) != solution(i, j):
            print(i, j)