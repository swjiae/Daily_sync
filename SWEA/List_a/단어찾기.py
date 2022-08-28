TC = int(input())
for T in range(1, TC+1):
    n, k = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]

    def count_row(i):
        cnt = 0
        total = 0
        for x in range(n):
            if arr[i][x] == 1:
                cnt += 1
            if arr[i][x] == 0:
                if cnt == k:
                    total += 1
                cnt = 0
        if cnt == k:
            total += 1
        return total

    def count_col(i):
        cnt = 0
        total = 0
        for y in range(n):
            if arr[y][i] == 1:
                cnt += 1
            if arr[y][i] == 0:
                if cnt == k:
                    total += 1
                cnt = 0
        if cnt == k:
            total += 1
        return total

    result = 0
    for i in range(n):
        result += count_row(i)
        result += count_col(i)

    print(f'#{T} {result}')