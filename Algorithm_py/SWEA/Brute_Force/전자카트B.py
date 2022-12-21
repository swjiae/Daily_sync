# 최소 배터리 사용량
def dfs(level, sum, prev):
    global N, Min
    if sum >= Min: # 이미 Min 보다 크면 돌릴 필요 없음 -> 시간, 메모리 절약
        return
    if level == N-1:
        sum += arr[prev][0] # 관리구역에서 사무실로 돌아갈 때 소비량 추가
        Min = min(Min, sum)
        return
    for i in range(1, N):
        if used[i] == 1: continue # 방문했던 관리구역 다시 갈 필요 없음
        used[i] = 1 # 방문한 관리구역 표시
        dfs(level+1, sum+arr[prev][i], i) # 현재 방문한 곳이 다음 level에서 prev
        used[i] = 0 # back할때 방문표시 리셋

# 입력받기
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
used = [0]*N
Min = 21e8
dfs(0, 0, 0)

print(Min)