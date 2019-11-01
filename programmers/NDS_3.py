# 비커 세개, 용량 달라, d 리터 만들기
# 가득 채우거나 비우거나 다른데 가득 채워주거나 등


#73.9점 짜리 답, 효율성에서 하나빼고 통과 불가 정확성에서 두 개 틀림
def gcd(a, b, c):
    for i in range(100, 0, -1):
        if a % i == b % i == c % i == 0:
            return i
def solution(a, b, c, d):
    answer = -1
    g = gcd(a, b, c)
    if d % g != 0 or d > max(a, b, c):
        return -1
    queue = [(0, 0, 0)]
    while True:
        x, y, z = queue.pop(0)
        if x * a + y * b + z * c == d:
            answer = 0
            if x:
                answer += (2 * abs(x) - 1)
            if y:
                answer += (2 * abs(y) - 1)
            if z:
                answer += (2 * abs(z) - 1)
            break
        elif x * a + y * b + z * c < d:
            queue.append((x + 1, y, z))
            queue.append((x, y + 1, z))
            queue.append((x, y, z + 1))
        else:
            queue.append((x - 1, y, z))
            queue.append((x, y - 1, z))
            queue.append((x, y, z - 1))
    return answer


# -- 코드를 입력하세요
# SELECT ID
# FROM GAME_USERS
# ORDER BY DISTANCE DESC, TIME_SPENT
# LIMIT 50;