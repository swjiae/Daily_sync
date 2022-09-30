T = int(input())
for t in range(1, T+1):
    # TC 입력받기
    N, B = map(int, input().split()) # N: 점원 수 B: 선반 높이
    height = list(map(int, input().split()))

    # 탑을 만들 수 있는 모든 조합 구하기
    # 결과(S (>=B, 키의 합) - B) 반환
    Min = 21e8
    def dfs(level, start, sum):
        global Min
        if sum >= B:
            Min = min(Min, sum-B)
        for i in range(start, N):
            dfs(level+1, i+1, sum+height[i])

    dfs(0, 0, 0)
    # 결과 출력하기
    print(f'#{t}', Min)
