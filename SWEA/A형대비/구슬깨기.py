# 부딪힐 수 있는 벽돌 top = []
# index : 열
# value : 행
# dfs로 level == N 만큼 확인
# top 갱신해주기
'''
1. 탑 벽돌 찾기
2. dfs 돌리면서 level == N 까지 완전탐색
3. 와중에 bomb함수를 통해 top 갱신하기
'''
N, W, H = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(H)]
top = [0]*W
for i in range(W):
    for j in range(H):
        if arr[j][i] != 0:
            top[i] = j
            break

'''
3 10 10
0 0 0 0 0 0 0 0 0 0
1 0 1 0 1 0 0 0 0 0
1 0 3 0 1 1 0 0 0 1
1 1 1 0 1 2 0 0 0 9
1 1 4 0 1 1 0 0 1 1
1 1 4 1 1 1 2 1 1 1
1 1 5 1 1 1 1 2 1 1
1 1 6 1 1 1 1 1 2 1
1 1 1 1 1 1 1 1 1 5
1 1 7 1 1 1 1 1 1 1
'''