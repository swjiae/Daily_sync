N, r, c = map(int, input().split())

def rec(N, r, c):
    if N == 0:
        return 0

    # 2 * (r % 2) + (c % 2) 행바뀌면*2 열바뀌면+1
    # 4 * rec(N - 1, r // 2, c // 2) 사분면 바뀌면+4
    return 2 * (r % 2) + (c % 2) + 4 * rec(N - 1, r // 2, c // 2)

result = rec(N, r, c)
print(result)