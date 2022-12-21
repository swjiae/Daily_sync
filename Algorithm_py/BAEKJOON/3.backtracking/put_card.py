n = int(input())
k = int(input())
numbers = [int(input()) for _ in range(n)]
path = []
used = [0] * n
possible = []
def dfs(level):
    global n, k, possible
    if level == k:
        string = ''
        for i in path:
            string += str(i)
        if string not in possible:
            possible.append(string)
        return
    for i in range(n):
        if used[i] == 1: continue
        used[i] = 1
        path.append(numbers[i])
        dfs(level+1)
        path.pop()
        used[i] = 0

dfs(0)
print(len(possible))