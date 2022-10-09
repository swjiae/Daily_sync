# 4명이 놀이동산에 갔습니다. [M B T I]
# 놀이기구를 타는데 1 unit에 3명이 앉을 수 있습니다.
# 4명중에 1명이 고소공포증이 있어서 놀이기구를 안탄다고 합니다.
# 놀이기구를 탈 조합을 모두 출력해 주세요.

person = ['M', 'B', 'T', 'I']
# level = 3
# brunch = 4
path = ['']*3
def dfs(level, start):
    if level == 3:
        for i in range(3):
            print(path[i], end='')
        print()
        return
    for i in range(start, 4):
        path[level] = person[i]
        dfs(level+1, i+1)

dfs(0, 0)
