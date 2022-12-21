TC = 10
for T in range(1, TC+1):
    n = int(input()) # 덤프횟수
    height = list(map(int, input().split())) # 각 상자의 높이

    for _ in range(n):
        idx_x = height.index(max(height))
        idx_n = height.index(min(height))
        height[idx_x] -= 1
        height[idx_n] += 1

    result = max(height) - min(height)

    print(f'#{T} {result}')