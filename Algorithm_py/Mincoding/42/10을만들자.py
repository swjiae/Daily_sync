arr = [i for i in range(1, 10)]
N = int(input())
cnt = 0
def dfs(level, sum):
    global N, cnt
    if level == N:
        if sum == 10:
            cnt += 1
        return
    for i in range(1, 10):
        dfs(level+1, sum+i)

dfs(0, 0)
print(cnt)