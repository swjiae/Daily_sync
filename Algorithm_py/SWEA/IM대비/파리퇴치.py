TC = int(input())
for T in range(1, TC+1):
    N, M = map(int, input().split()) # N: NxN 배열 # M: MXM 파리채

    arr = [list(map(int, input().split())) for _ in range(N)]

    def flies(y, x):
        total = 0
        for i in range(y, y+M):
            for j in range(x, x+M):
                if 0 <= i < N and 0 <= j < N:
                    total += arr[i][j]
        return total

    Max = 0
    for y in range(N):
        for x in range(N):
            ret = flies(y, x)
            if ret > Max:
                Max = ret

    print(f'#{T} {Max}')