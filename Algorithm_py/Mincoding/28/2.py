N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

# 현수(0)의 직속 보스와 직속 부하 출력

boss = []
under = []
for i in range(N):
    if arr[0][i] == 1:
        under.append(i)
    if arr[i][0] == 1:
        boss.append(i)

print(boss, under)