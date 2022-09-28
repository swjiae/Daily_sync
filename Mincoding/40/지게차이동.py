'''
0 3 5 1
1 1 1 5
1 50 20 10
1 50 5 0
'''
arr = [list(map(int, input().split())) for _ in range(4)]
direct = [[0]*4 for _ in range(4)]
for i in range(1, 4):
    arr[i][0] += arr[i-1][0]
    arr[0][i] += arr[0][i-1]
    direct[i][0] = 1 # up
    direct[0][i] = 2 # left

for i in range(1, 4):
    for j in range(1, 4):
        up = arr[i-1][j]
        left = arr[i][j-1]

        if up < left:
            tmp1 = up
            tmp2 = 1
        else:
            tmp1 = left
            tmp2 = 2
        arr[i][j] += tmp1
        direct[i][j] = tmp2

result = []
y, x = 3, 3
while 1:
    result.append([f'{y},{x}'])
    if y == 0 and x == 0:
        break
    if direct[y][x] == 1:
        y -= 1
    else:
        x -= 1

for i in range(len(result)-1, -1, -1):
    print(*result[i])

