# 크레이지 아케이드
# 1 폭탄
# 3 벽
# 0의 개수

arr = [
    [0, 0, 0, 0, 0],
    [0, 1, 3, 1, 0],
    [0, 3, 1, 0, 0],
    [0, 1, 3, 1, 0],
    [0, 0, 0, 0, 0]
]

N = len(arr)

# 폭탄 터트리기
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
def bomb(y, x):
       for i in range(4):
              for j in range(N):
                     ny = y + dy[i] * j
                     nx = x + dx[i] * j
                     if 0 <= ny < N and 0 <= nx < N:
                            if arr[ny][nx] == 1:
                                   continue
                            if arr[ny][nx] == 3:
                                   break
                            arr[ny][nx] = 2

# 폭탄 위치 찾기
for y in range(N):
       for x in range(N):
              if arr[y][x] == 1:
                     bomb(y, x)

# 안전구역 카운트
cnt = 0
for i in range(N):
       for j in range(N):
              if arr[i][j] == 0:
                     cnt += 1

print(arr)
print(cnt)