'''
0 0 3 3 0 0 1 1
2 1 1 2 0 0 2 2
1 1 2 3 9 1 3 3
0 0 1 1 0 0 4 4
'''

arr = [list(map(int, input().split())) for _ in range(4)]

def rect(y, x):
    Sum = 0
    len_y = 0
    for i in range(y, 4):
        len_y += 1
        len_x = 0
        for j in range(x, 8):
            len_x += 1
            if 0 <= i < 4 and 0 <= j < 8:
                if arr[i][j] == 0:
                    return Sum
                else:
                    Sum += arr[i][j]
    return Sum

Max = 21e-8
for y in range(4):
    for x in range(8):
        if arr[y][x] != 0:
            result = rect(y, x)
            if result > Max:
                Max = result

print(Max)