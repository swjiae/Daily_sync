Map = [list(map(int, input().split())) for _ in range(4)]
for i in range(1, 4):
    Map[0][i] += Map[0][i-1]
    Map[i][0] += Map[i-1][0]

'''
[[0, 3, 8, 9], 
 [1, 1, 1, 5], 
 [2, 50, 20, 10], 
 [3, 50, 5, 0]]
'''
answer=[]

for i in range(1, 4):
    for j in range(1, 4):
        Map[i][j] += min(Map[i-1][j], Map[i][j-1])

print(Map)
