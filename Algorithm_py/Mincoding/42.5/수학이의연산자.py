from collections import deque

# 입력받기
N = int(input())
number = list(map(int, input().split()))
operator = ['!!', '#', '$', '&']

# 계산기 만들기
def cal(path): # ['!!', '!!']
    q = deque(number)
    while len(q) >= 2:
        a, b = q.popleft(), q.popleft()
        o = path.pop()
        if o == '!!':
            result = (a-b) * (a+b)
        elif o == '#':
            result = max(a, b)
        elif o == '$':
            result = a**2 - b**2
        elif o == '&':
            result = (a+b) ** 2
        q.appendleft(result)

    final = q[0]
    return 1 if final == 100 else 0

# dfs로 연산자 고르기
path = ['']*(N-1)
p = []
cnt = 0
def dfs(level):
    global cnt
    if level == N-1:
        for i in range(N-1):
            p.append(path[i])
        cnt += cal(p)
        return
    for i in range(4):
        path[level] = operator[i]
        dfs(level+1)

dfs(0)

# 결과 출력하기
print(cnt)