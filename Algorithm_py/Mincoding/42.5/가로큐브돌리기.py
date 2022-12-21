N = int(input())
cube = [list(map(int, input().split())) for _ in range(N)]
arr = []

def dfs(y, x, sum):
    if y == N:
        arr.append(sum)
        return
    for i in range(N):
        k = (x+i) % N
        dfs(y+1, x, sum+cube[y][k])

for i in range(N):
    dfs(1, i, cube[0][i])


Max = 0
for x in range(N**(N-1)):
    res = 1
    for i in range(0, N**N, N**(N-1)):
        res *= arr[i+x]
    if res > Max:
        Max = res
print(f'{Max}점')
'''
4
-1 2 3 3
-9 8 9 0
-1 -9 1 4
5 3 1 2
'''