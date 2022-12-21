# flag 바꿔가며 확인하기
def repaint(y, x):
    cnt = 0
    flag = arr[y][x]
    for i in range(y, y+8):
        for j in range(x, x+8):
            if arr[i][j] != flag:
                cnt += 1
            flag = not(flag)
        flag = not(flag)
    return min(cnt, 64-cnt)

# 배열 입력받기
M, N = map(int, input().split())
arr = [list(input()) for _ in range(M)]

# 배열 0(black)과 1(white)로 표현하기
for y in range(M):
    for x in range(N):
        if arr[y][x] == 'B':
            arr[y][x] = 0
        else:
            arr[y][x] = 1

# 8 * 8 배열 자르기
Min = 21e8
for y in range(M-7):
    for x in range(N-7):
        result = repaint(y, x)
        Min = min(Min, result)

print(Min)