TC = int(input())
for tc in range(1, TC+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    # 행 기준
    maxV = 0
    for i in range(N):
        cnt = 0
        for j in range(M):
            if arr[i][j]:
                cnt += 1
                if maxV < cnt:
                    maxV = cnt
            else:
                cnt = 0

    # 열 기준
    for j in range(M):
        cnt = 0
        for i in range(N):
            if arr[i][j]:
                cnt += 1
                if maxV < cnt:
                    maxV = cnt
            else:
                cnt = 0