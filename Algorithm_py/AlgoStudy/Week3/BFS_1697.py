N, K = map(int, input().split())
visit = [0]*100001
queue = [(N, 0)]

while queue:
    N, level = queue.pop(0)
    if N == K:
        print(level)
        break
    if N > K and level == 0:
        print(N-K)
        break
    for i in (N+1, N-1, N*2):
        if 0 <= i <= 100000 and visit[i] == 0:
            queue.append((i, level+1))
            visit[i] = 1