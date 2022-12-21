n=input()
m=input()

dp=[[0]*(len(n)+1) for _ in range(len(m)+1)]

for i in range(1,len(n)+1):
    for j in range(1,len(m)+1):
        if n[i-1]==m[j-1]:
            dp[i][j]=dp[i-1][j-1]+1
            answer=dp[i][j]
        else:
            dp[i][j]=max(dp[i-1][j],dp[i][j-1])
            answer=dp[i][j]

print(answer)

'''
BABJYP
ABPABY
'''