monster = ['A', 'C', 'D']
MAP = [list(input()) for _ in range(4)]
directy = [0, 1, 0, -1, 0] # 우하좌상우
directx = [1, 0, -1, 0, 1]

for m in monster:
    for y in range(4):
        for x in range(3):
            if m == MAP[y, x]:

