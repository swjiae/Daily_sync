power=[50, 40, 99, 5, 25, 6, 37]

# 서바이벌 게임
# a ~ g 를 두 팀으로 나누어서 
# 게임을 하고자 합니다.
# 두 팀으로 나누었을 때
# 두 팀의 전투력 차이가 최소가 되었을 때
# 최소 전투력 차이는 몇일까요?
# 모든 선수는 경기에 참가를 하며
# 1인팀도 가능 합니다.

power=[50,40,99,5,25,6,37]
check=[0]*7
Min=21e8

def dfs(start,level,sum):
    global Min,power
    against=0
    for i in range(7):
        if check[i]==0:
            against+=power[i]
    gap=abs(sum-against)
    Min=min(Min,gap)

    if level==7:
        return
    for i in range(start,7):
        check[i]=1
        dfs(i+1,level+1,sum+power[i])
        check[i]=0
dfs(0,0,0) # start,level,sum
print(Min)