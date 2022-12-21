machine = [
    ['A', 'B', 'C', 'E', 'F', 'G'],
    ['H', 'I', 'J', 'K', 'L', 'M'],
    ['N', 'O', 'P', 'Q', 'R', 'S']
    ]

result = [
    ['A', 'B', 'C', 'E', 'F', 'G'],
    ['H', 'I', 'J', 'K', 'L', 'M'],
    ['N', 'O', 'P', 'Q', 'R', 'S']
]

arr = list(input())

def Turn(y, x):
    directy = [0, -1, 1, 0, 0]
    directx = [0, 0, 0, -1, 1]
    for i in range(5):
        dy = y + directy[i]
        dx = x + directx[i]
        if 0 <= dy < 3 and 0 <= dx < 6:
            if result[dy][dx] != '#':
                result[dy][dx] = '#'
            else:
                result[dy][dx] = machine[dy][dx]


for y in range(3):
    for x in range(6):
        for a in range(len(arr)):
            if machine[y][x] == arr[a]:
                Turn(y, x)

for i in range(3):
    print(*result[i], sep='')
