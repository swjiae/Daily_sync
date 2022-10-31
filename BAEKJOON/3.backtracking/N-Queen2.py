N = int(input())
arr = [0] * N

def possible(y): # level = y
    for i in range(y):
        if arr[y] == arr[i] or abs(arr[y] - arr[i]) == abs(y - i):
            return 0
    return 1

cnt = 0
def dfs(level): 
    global cnt
    if level == N:
        cnt += 1
        return
    for x in range(N):
        arr[level] = x
        if possible(level):
            dfs(level+1)

dfs(0)
print(cnt)