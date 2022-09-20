# 입력받기
feed = list(map(int, input().split()))
turn = int(input())
visited = [0]*6
Max = 0
def dfs(level, sum):
    global Max
    if level // 3 == turn:
        print(sum)
        Max = max(Max, sum)
        return

    # 첫 번째 독수리
    if level % 3 == 0:
        if level > 0:
            feed.append(feed.pop(0)*2)
        for i in range(3):
            if visited[i] == 1: continue
            visited[i] = 1
            dfs(level+1, sum+feed[i])
            visited[i] = 0

    # 두 번째 독수리
    if level % 3 == 1:
        for i in range(3, 6):
            if visited[i] == 1: continue
            visited[i] = 1
            dfs(level+1, sum+feed[i])
            visited[i] = 0

    # 세 번째 독수리
    if level % 3 == 2:
        for i in range(1, 5):
            if visited[i] == 1: continue
            dfs(level+1, sum+feed[i])
            visited[i] = 0

print(Max)