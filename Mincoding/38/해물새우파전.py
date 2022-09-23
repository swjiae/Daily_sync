# 입력받기
arr = [list(map(int, input())) for _ in range(7)]

# 새우랑 오징어 리스트 만들기
sh = []
sq = []
for i in range(7):
    for j in range(7):
        if arr[i][j] == 1:
            sh.append([i, j])
        elif arr[i][j] == 2:
            sq.append([i, j])

# 거리 확인하는 함수 만들기 (fail 이면 0 리턴)
def distance(sy, sx, ey, ex, k):
    if sy == ey:
        if abs(sx-ex) < k:
            return 0
    if sx == ex:
        if abs(sy-ey) < k:
            return 0
    else:
        return 1

# pass / fail 확인하기
flag = 1
for i in range(len(sh)-1):
    flag = distance(sh[i][0], sh[i][1], sh[i+1][0], sh[i+1][1], 3)
    if flag == 0:
        break
flag2 = 1
for i in range(len(sq)-1):
    flag2 = distance(sq[i][0], sq[i][1], sq[i+1][0], sq[i+1][1], 4)
    if flag2 == 0:
        break

# 결과 출력하기
print('pass' if flag and flag2 else 'fail')
