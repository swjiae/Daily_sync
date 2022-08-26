n = int(input())
number = [list(map(int, input().split())) for _ in range(n)]
bit = [list(map(int, input().split())) for _ in range(n)]

tmp = []
for y in range(n):
    for x in range(n):
        if bit[y][x] == 1:
            tmp.append(number[y][x])

result = sorted(tmp, key=lambda x: (-tmp.count(x), x))

print(*result)