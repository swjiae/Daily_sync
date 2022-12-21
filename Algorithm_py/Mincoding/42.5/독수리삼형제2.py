from copy import deepcopy
# 입력받기
feed = list(map(int, input().split()))
turn = int(input())


def change():
    global feed
    for i in range(len(feed)):
        if feed[i] != 0:
            feed[i] *= 2

# DFS를 통해 먹이 크기 max 값 찾기
Max = 0
def dfs(level, sum):
    global feed, Max
    if level // 3 == turn:
        Max = max(Max, sum)
        return

    # 첫 번째 독수리
    bu = deepcopy(feed)
    if level % 3 == 0:
        for i in range(3):
            tmp = 0
            if feed[i] != 0:
                tmp = feed[i]
                feed[i] = 0
            dfs(level+1, sum+tmp)
            feed = deepcopy(bu)

    # 두 번째 독수리
    if level % 3 == 1:
        for i in range(3, 6):
            tmp = 0
            if feed[i] != 0:
                tmp = feed[i]
                feed[i] = 0
            dfs(level+1, sum+tmp)
            feed = deepcopy(bu)

    # 세 번째 독수리
    if level % 3 == 2:
        for i in range(1, 5):
            tmp = 0
            if feed[i] != 0:
                tmp = feed[i]
                feed[i] = 0
            change()
            dfs(level+1, sum+tmp)
            feed = deepcopy(bu)

dfs(0,0)
print(Max)