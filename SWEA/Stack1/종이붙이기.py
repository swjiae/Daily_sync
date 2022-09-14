TC = int(input())
for T in range(1, TC+1):
    arr = [10, 20]
    N = int(input())
    cnt = 0
    stack = []
    def dfs(n):
        global cnt
        if n > N:
            return
        if n == N:
            cnt += 2 ** stack.count(20)
            return
        for i in range(2):
            stack.append(arr[i])
            dfs(n+arr[i])
            stack.pop()
    dfs(0)
    print(f'#{T} {cnt}')


