N, M = map(int, input().split())
Map = [list(input()) for _ in range(N)]

used = [[0]*M for _ in range(N)]
def BFS(y, x):
    used[y][x] = 1
    queue = [(y, x)]
    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]
    cnt = 0

    while queue:
        y, x = queue.pop(0)
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < N and 0 <= nx < M:
                if Map[ny][nx] == 'X': continue
                if used[ny][nx] == 1: continue
                if Map[ny][nx] == 'P':
                    cnt += 1
                queue.append((ny, nx))
                used[ny][nx] = 1
    return cnt

result = 0
for i in range(N):
    for j in range(M):
        if Map[i][j] == 'I':
            result = BFS(i, j)

if result:
    print(result)
else:
    print('TT')

