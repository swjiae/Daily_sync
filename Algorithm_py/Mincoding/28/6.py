word = input()
n = len(word)
arr = [list(map(int, input().split())) for _ in range(n)]

def dfs(now):
    print(word[now], end="")
    for i in range(n):
        if arr[now][i] == 1:
            dfs(i)

dfs(0)