'''
1. brunch = 3x3
2. level = 3
3. bomb 조합 함수 만들기
4. getcnt 함수 만들기
5. backtracking / used 사용하기
'''
from copy import deepcopy
Map = [list(input()) for _ in range(4)] # 적 위치 표시 배열
N = int(input()) # 폭탄 투하 횟수
path = ['']*3
used = [[0]*4 for _ in range(4)]
def getcnt(y, x):
    global used
    cnt = 0
    dy = [0, -1, 1, 0, 0]
    dx = [0, 0, 0, -1, 1]
    for i in range(5):
        ny = y + dy[i]
        nx = x + dx[i]
        if 0 <= ny < 4 and 0 <= nx < 4:
            if Map[ny][nx] != '_' and used[ny][nx] == 0:
                used[ny][nx] = 1
                cnt += 1
    return cnt

Max = 0
result = []
def bomb(level, total):
    global Max, Map, used, result
    bu1 = deepcopy(used)
    if level == 3:
        if total > Max:
            Max = total
            result = deepcopy(path)
        return
    for i in range(4):
        for j in range(4):
            if Map[i][j] != '_':
                path[level] = Map[i][j]
                cnt = getcnt(i, j)
                bu2 = deepcopy(Map)
                Map[i][j] = '_'
                bomb(level+1, total+cnt)
                Map = deepcopy(bu2)
                used = deepcopy(bu1)

bomb(0, 0)
print(*sorted(result))