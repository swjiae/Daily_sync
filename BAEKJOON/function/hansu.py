N = int(input())

def hansu(N):
    num = list(str(N))
    for i in range(len(num)):
        num[i] = int(num[i])
    sub = num[0] - num[1]
    for i in range(1, len(num)-1):
        if num[i] - num[i+1] != sub:
            return 0
        return 1

if N < 100:
    print(N)
else:
    cnt = 0
    for N in range(100, N+1):
        cnt += hansu(N)
    print(99+cnt)