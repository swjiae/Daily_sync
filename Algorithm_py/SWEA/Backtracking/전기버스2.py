from collections import deque

# 최소 충전 횟수 구하는 함수
def bfs(start, end):
    q = deque()
    q.append([start, charge[start], 0]) # 시작점, 충전량, 충전횟수
    check = [0]*(end+1)
    check[start] = 1
    while q:
        start, move, level = q.popleft()
        for i in range(1, move+1):
            if start <= start+i <= end:
                check[start+i] = 1
                if start <= start+i < end:
                    q.append([start+i, charge[start+i], level+1])
        if check[end] == 1:
            return level

# 입력받기
TC = int(input())
for T in range(1, TC+1):
    arr = list(map(int, input().split()))
    end = arr[0]-1 # 도착지 idx
    charge = arr[1:len(arr)] # 충전소 list
    result = bfs(0, end)
    print(f'#{T}', result)