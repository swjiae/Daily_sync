TC = int(input())
for T in range(1, TC+1):
    arr = [list(map(int, input().split())) for _ in range(9)]
    check = [i for i in range(1, 10)]
    result = 0
    # 행
    for i in range(9):
        used = []
        for j in range(9):
            used.append(arr[i][j])
        result += 1 if sorted(used) == check else 0

    # 열
    for i in range(9):
        used = []
        for j in range(9):
            used.append(arr[j][i])
        result += 1 if sorted(used) == check else 0

    # 3X3
    def pattern(y, x):
        global result
        used = []
        for i in range(y, y+3):
            for j in range(x, x+3):
                used.append(arr[i][j])
        result += 1 if sorted(used) == check else 0

    for y in range(0, 9, 3):
        for x in range(0, 9, 3):
            pattern(y, x)

    answer = 1 if result == 27 else 0

    print(f'#{T} {answer}')