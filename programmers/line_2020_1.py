def solution(boxes):
    answer = len(boxes)
    product = [False] * 1000001
    for i in boxes:
        for j in i:
            if not product[j]:
                product[j] = True
            else:
                answer -= 1
                product[j] = False
    return answer