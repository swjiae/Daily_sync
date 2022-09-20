from collections import deque

name = ['cs', 'language', 'datastructure', 'algorithm', 'project', 'coding test', 'to be a programmer']

arr = [
    [0, 0, 0, 0, 0, 0, 1],
    [0, 0, 1, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 0, 0],
]

acc = [0]*7
used = [0]*7

q = deque()
for j in range(7):          # 사전 작업 개수 등록
    for i in range(7):
        if arr[i][j] == 1:
            acc[j] += 1

for i in range(7):          # 바로 작업 착수 가능한 것들은
    if acc[i] == 0:           # used에 1체크 하고 q에 등록
        used[i] = 1
        q.append(i)

result = []
while q:
    now = q.popleft()
    result.append(name[now])       # 행 : 선행 과제 / 열 : 후행 과제
    for i in range(7):
        if arr[now][i] == 1 and used[i] == 0:
            if acc[i] == 1:
                used[i] = 1
                acc[i] -= 1
                q.append(i)
            else:
                acc[i] -= 1

print(*result)