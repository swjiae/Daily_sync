N, M = map(int, input().split())
cards = list(map(int, input().split()))
Max = 0
def dfs(level, sum, start):
    global N, M, Max
    if sum > M: return
    if level == 3:
        Max = max(Max, sum)
        return
    for i in range(start, N):
        dfs(level+1, sum+cards[i], i+1)

dfs(0, 0, 0)

print(Max)