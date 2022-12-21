from collections import deque

degree = int(input()) # 180
move = degree // 90

q = deque([12, 9, 6, 3])
for _ in range(move):
    q.append(q.popleft())

idx = [0, 1, 3, 2]

for i in idx:
    print(q[i], end=' ')
