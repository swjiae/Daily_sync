n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
path = [0]

def dfs(now, level):
    if level == 2:
        for i in range(3):
            print(path[i], end=" ")
        print()
        return
    for i in range(len(arr)):
        if arr[now][i] == 1:
            path.append(i)
            dfs(i, level+1)
            path.pop()
dfs(0, 0)
