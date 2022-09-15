line1=[3,7,1,-3,-6,1]
line2=[7,-4,1,-5,3,2]
used1=[0]*6
used2=[0]*6

Min=21e8
answer=21e8

def dfs(level,sum):
    global Min,answer,used1,used2
    if level==12:
        # 0에 가장 가까운 sum
        if Min>abs(sum):
            Min=abs(sum)
            answer=sum
        return

    if level%2==0:
        for i in range(6):
            if used1[i]==1: continue
            used1[i]=1
            dfs(level+1,sum+(line1[i]*(level+1)))
            used1[i]=0
    else:
        for i in range(6):
            if used2[i]==1: continue
            used2[i]=1
            dfs(level+1,sum+(line2[i]*(level+1)))
            used2[i]=0

dfs(0,0) #level,sum
print(answer)