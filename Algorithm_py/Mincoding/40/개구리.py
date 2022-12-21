Map = [list(map(int, input().split())) for _ in range(7)]

dy = [-1, -1, -1]
dx = [-1, 0, 1]
for i in range(1, 7):
    for j in range(3):
        Max = 0
        if Map[i][j] == 0: continue
        for k in range(3):
            py = i + dy[k]
            px = j + dx[k]
            if 0 <= py < 7 and 0 <= px < 3:
                if Map[py][px] == 0: continue
                Max = max(Max, Map[py][px])
        Map[i][j] += Max

result = max(Map[-1])
print(result)

