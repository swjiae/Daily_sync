from collections import deque
# 입력받기
Map = [list(map(int, input().split())) for _ in range(4)]

# 개체수 많은 것 카운트 하기
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
def bfs(y, x, K):
    cnt = 0
    q = deque()
    q.append([y, x])
    Map[y][x] = ''
    while q:
        y, x = q.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < 4 and 0 <= nx < 9:
                if Map[ny][nx] == K:
                    Map[ny][nx] = ''
                    q.append([ny, nx])
        cnt += 1
    return cnt

Max = 0
for i in range(4):
    for j in range(9):
        for K in range(4):
            if Map[i][j] == K:
                tmp = bfs(i, j, K)
                if tmp > Max:
                    Max = tmp
                    num = K

# 개체수 * 숫자 출력하기
print(Max*num)