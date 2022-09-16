from collections import deque

arr = [
    [0, 1, 0, 1, 0, 0],
    [0, 0, 1, 0, 1, 0],
    [0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],

]
name = list(input().split()) # A B C D E F
answer = []
def bfs(st):
    global answer
    q = deque()
    q.append(st)
    while q:
        now = q.popleft()
        answer.append(name[now])
        for i in range(6):
            if arr[now][i] == 1:
                q.append(i)

bfs(0)
print(*answer)