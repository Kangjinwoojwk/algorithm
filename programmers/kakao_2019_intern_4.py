# 정답은 맞지만 효율성 전부 fail

def solution(k, room_number):
    hotel = [True] * (k + 1)
    answer = []
    for i in room_number:
        if not hotel[i]:
            while not hotel[i]:
                i += 1
        hotel[i] = False
        answer.append(i)
    return answer