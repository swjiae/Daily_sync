# 각 항에서 1~4 사이의 숫자를 1개씩 택해서 다
# 더했을떄 10이 나오는 경우는 몇가지 인가요?
# n 개의 항에서 1~4 사이의 숫자를 택할 것입니다.

N = int(input())
cnt = 0
def dfs(level, sum):
    global cnt
    if level == N:
        if sum == 10:
            cnt += 1
        return
    for i in range(1, 5):
        dfs(level+1, sum+i)

total = 0
def dfs2(level, sum):
    global total
    if level == N:
        if sum == 10:
            total += 1
        return
    dfs2(level+1, sum+1)
    dfs2(level+1, sum+2)
    dfs2(level+1, sum+3)
    dfs2(level+1, sum+4)

dfs(0, 0)
dfs2(0, 0)

print(cnt, total)