computer = int(input())
branch = int(input())
arr = [[] for _ in range(computer)]
used = [0]*computer
cnt = 0

for _ in range(branch):
    a, b = map(int, input().split())
    arr[a-1].append(b-1)
    arr[b-1].append(a-1)

def bfs(start):
    global cnt
    queue = [start]
    while queue:
        now = queue.pop(0)
        for nxt in arr[now]:
            if used[nxt] == 0:
                used[nxt] = 1
                queue.append(nxt)
                cnt += 1

used[0] = 1
bfs(0)
print(cnt)