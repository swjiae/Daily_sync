N = int(input())
mou = [list(map(int, input().split())) for _ in range(N)]
flag = 0
def move(y, x):
    global flag
    if mou[N-1][N-1] == 1:
        flag = 1
        return
    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if 0 <= ny < N and 0 <= nx < N:
            if mou[ny][nx] == 1: continue
            mou[ny][nx] = 1
            move(ny, nx)
            mou[ny][nx] = 0

move(0, 0)
print('가능' if flag else '불가능')



