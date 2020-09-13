def solution(ball, order):
    answer = []
    preorder = []
    for i in order:
        while ball[0] in preorder:
            preorder.remove(ball[0])
            answer.append(ball.pop(0))
        while ball[-1] in preorder:
            preorder.remove(ball[-1])
            answer.append(ball.pop())
        if i == ball[0]:
            answer.append(ball.pop(0))
        elif i == ball[-1]:
            answer.append(ball.pop())
        else:
            preorder.append(i)
    return answer