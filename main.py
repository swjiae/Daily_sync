power=[50, 40, 99, 5, 25, 6, 37]

# 서바이벌 게임
# a ~ g 를 두 팀으로 나누어서
# 게임을 하고자 합니다.
# 두 팀으로 나누었을 때
# 두 팀의 전투력 차이가 최소가 되었을 때
# 최소 전투력 차이는 몇일까요?
# 모든 선수는 경기에 참가를 하며
# 1인팀도 가능 합니다.

path=['']*7
sum=0
team=['O','X']
Min = 21e8
for i in range(7):
    sum+=power[i]
def dfs(level):
    global Min, sum
    if level==7:
        if len(set(path)) == 1: return
        teama=0
        for i in range(7):
            if path[i]=='O':
                teama+=power[i]
        cha=abs(sum-teama-teama)
        Min = min(Min, cha)
        return

    for i in range(2):
        path[level]=team[i]
        dfs(level+1)
        path[level]=''

dfs(0)
print(Min)
