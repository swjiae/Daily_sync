# + 모양
directy1 = [-1, 1, 0, 0] # 상하좌우
directx1 = [0, 0, -1, 1]
# x 모양
directy2 = [1, 1, -1, -1] # 동남부터 시계방향
directx2 = [1, -1, -1, 1]

TC = int(input())
for T in range(1, TC+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    maxV = 0
    for y in range(N):
        for x in range(N):
            # + 모양
            cnt1 = arr[y][x]
            for k in range(4): # 방향 정하기
                for z in range(1, M): # 뻗어나갈 칸 수 정하기
                    dy, dx = y + directy1[k]*z, x + directx1[k]*z
                    if 0 <= dy < N and 0 <= dx < n:
                        cnt1 += arr[dy][dx]
            if maxV < cnt1:
                maxV = cnt1
