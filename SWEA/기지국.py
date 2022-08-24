TC = int(input())
for T in range(1, TC+1):
    N = int(input())
    arr = [list(input()) for _ in range(N)]

    # 커버된 집 체크하는 함수 만들기
    # for i in range(4):
    # for j in range(1, ord(arr[i][j])+2):
    # dy = y + dys[i] * j
    # dx = x + dxs[i] * j
    def Covered(y, x, a):
        na = ord(a) - 65
        for n in range(na+1):
            dys = [-1-n, 1+n, 0, 0]
            dxs = [0, 0, -1-n, 1+n]
            for i in range(4):
                dy = y + dys[i]
                dx = x + dxs[i]
                if 0 <= dy < N and 0 <= dx < N:
                    if arr[dy][dx] == 'H':
                        arr[dy][dx] = 'X'

    # 기지국 찾기
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 'A':
                Covered(i, j, 'A')
            elif arr[i][j] == 'B':
                Covered(i, j, 'B')
            elif arr[i][j] == 'C':
                Covered(i, j, 'C')

    # 커버되지 않은 집 카운트 세기
    uncovered = 0
    for i in arr:
        uncovered += i.count('H')

    print(f'#{T} {uncovered}')