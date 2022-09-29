a = 'aabbc'
b = 'eebbff'
a = list(input())
b = list(input())
cnt = 0
POP = []
def remov(a, b):
    global cnt
    for i in range(len(a)):
        if a[i] not in b:
            POP.append(a[i])
            cnt += 1

remov(a, b)
remov(b, a)
print(cnt)
