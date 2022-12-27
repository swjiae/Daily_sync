N = int(input())
arr = [list(map(int, input())) for _ in range(N)]
used = [[0]*N for _ in range(N)]

def bfs(y, x):
    used[y][x] = 1
    queue = []
    queue.append((y, x))
    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]
    cnt = 1

    while queue:
        yy, xx = queue.pop(0)
        for i in range(4):
            ny = yy + dy[i]
            nx = xx + dx[i]
            if 0 <= ny < N and 0 <= nx < N:
                if arr[ny][nx] == 0: continue
                if used[ny][nx] == 1: continue
                cnt += 1
                queue.append((ny, nx))
                used[ny][nx] = 1

    return cnt

result = []
for y in range(N):
    for x in range(N):
        if arr[y][x] != 0 and used[y][x] == 0:
            result.append(bfs(y, x))

result.sort()

print(len(result))

for i in range(len(result)):
    print(result[i])
