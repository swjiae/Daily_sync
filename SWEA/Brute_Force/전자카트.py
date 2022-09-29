from collections import deque
TC = int(input())
for T in range(1, TC+1):
    # 입력받기
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    # 가능한 경로의 에너지 소비량 구하기
    def Amount(path):
        total = 0
        q = deque(path)
        q.appendleft(0)
        while 1:
            if len(q) == 1:
                st = q.popleft()
                ed = 0
                total += arr[st][ed]
                return total
            st = q.popleft()
            ed = q.popleft()
            total += arr[st][ed]
            q.appendleft(ed)

    # dfs 이용하여 가능한 경로 & 최소값 구하기
    path = []
    used = [0]*(N)
    Min = 21e8
    def dfs(level):
        global N, Min
        if level == N-1:
            amount = Amount(path)
            Min = min(Min, amount)
            return
        for i in range(1, N):
            if used[i] == 1: continue
            path.append(i)
            used[i] = 1
            dfs(level+1)
            path.pop()
            used[i] = 0

    dfs(0)

    # 출력하기
    print(f'#{T}', Min)