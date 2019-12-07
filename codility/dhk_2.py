# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    data = dict()
    answer = 0
    for i in A:
        if i in data:
            data[i] += 1
        else:
            data[i] = 1
    for k, v in data.items():
        if k == v and k > answer:
            answer = k
    return answer