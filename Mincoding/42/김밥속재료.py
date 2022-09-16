arr = list(input())
path = ['']*3
def dfs(level, start):
    if level == 3:
        for i in range(3):
            print(path[i], end='')
        print()
        return
    for i in range(start, len(arr)):
        path[level] = arr[i]
        dfs(level+1, i)
        path
dfs(0, 0)
