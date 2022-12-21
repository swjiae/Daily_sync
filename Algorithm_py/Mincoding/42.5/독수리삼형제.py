from copy import deepcopy
# 입력받기
feed = list(map(int, input().split()))
turn = int(input())

# dfs를 통해 독수리 먹이 총 합 Max 구하기
Max = 0
def dfs(level, sum):
    global Max, feed
    # turn만큼 돌았으면 리턴
    if level // 3 == turn:
        Max = max(Max, sum)
        return

    # level == 3일 때(turn 1회 증가)마다 남은 먹이*2
    # if level > 0 and level % 3 == 0:
    #     feed.append(feed.pop(0) * 2)

    bu = deepcopy(feed)
    # 첫 번째 독수리
    if level % 3 == 0:
        for i in range(3):
            tmp = 0
            if feed[i] != 0:
                tmp = feed[i]
                feed[i] = 0
            dfs(level + 1, sum + tmp)
            feed = deepcopy(bu)

    # 두 번째 독수리
    if level % 3 == 1:
        for i in range(3, 6):
            tmp = 0
            if feed[i] != 0:
                tmp = feed[i]
                feed[i] = 0
            dfs(level + 1, sum + tmp)
            feed = deepcopy(bu)

    # 세 번째 독수리
    if level % 3 == 2:
        for i in range(1, 5):
            tmp = 0
            if feed[i] != 0:
                tmp = feed[i]
                feed[i] = 0
            # feed 두 배 만들기
            for i in range(len(feed)):
                if feed[i] != 0:
                    feed[i] *= 2
            dfs(level + 1, sum + tmp)
            feed = deepcopy(bu)

dfs(0,0)
print(Max)