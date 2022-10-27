M, N = map(int, input().split())
arr = [list(input()) for _ in range(M)]
Min = 21e8

# 비교할 배열 만들기
black = [['B']*8 for _ in range(8)]
white = [['W']*8 for _ in range(8)]
for i in range(8):
    if i % 2 == 0:
        for j in range(1, 8, 2):
            black[i][j] = 'W'
            white[i][j] = 'B'
    if i % 2 == 1:
        for j in range(0, 8, 2):
            black[i][j] = 'W'
            white[i][j] = 'B'
print(black)

# 조건에 맞는지 확인하는 함수
def check(y, x):
    bcnt, wcnt = 0, 0
    for i in range(y, y+8):
        for j in range(x, x+8):
            if arr[i][j] != black[i-y][j-x]:
                bcnt += 1
            if arr[i][j] != white[i-y][j-x]:
                wcnt += 1
    return min(bcnt, wcnt)

# 8 * 8 배열 자르기
for y in range(M-8+1):
    for x in range(N-8+1):
        result = check(y, x)
        Min = min(Min, result)

# Min 출력하기
print(Min)