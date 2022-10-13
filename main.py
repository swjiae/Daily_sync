from collections import deque

Map = [
    [1, 0, 1, 0, 0],
    [0, 0, 1, 0, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 1, 0, 0],
    [1, 1, 0, 1, 1]
]

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

print('큰 섬:',max(SIZE))
print('작은 섬:', min(SIZE))
print('총:', cnt)
