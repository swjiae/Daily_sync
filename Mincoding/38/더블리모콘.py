from collections import deque
S = int(input())
D = int(input())
used = [0]*100001
q = deque()
q.append([S, 0])
used[S] = 1
while q:
    S, level = q.popleft()
    if S == D:
        break
    for i in range(4):
        if i == 0:
            next = S + 1
        elif i == 1:
            next = S - 1
        elif i == 2:
            next = S // 2
        elif i == 3:
            next = S * 2
        if 0 <= next <= 100000:
            if used[next] == 1: continue
            q.append([next, level + 1])
            used[next] = 1

print(level)
