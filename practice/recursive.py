# def printHello(i, n):
#     if i == n: return
#
#     print(i, "Hello World!!")
#     printHello(i + 1, n)
#     print(i, "Hello World!!")
#
#
# printHello(0, 3)

cnt = 0
def printHello(i, n):
    global cnt
    if i == n:
        cnt += 1
    return
    printHello(i + 1, n)


printHello(0, 3)
print(cnt)