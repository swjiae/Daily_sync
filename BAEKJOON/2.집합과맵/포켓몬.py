N, M = map(int, input().split())
have = {}
for i in range(1, N+1):
    h = input()
    have[i] = h
    have[h] = i
for _ in range(M):
    check = input()
    if check.isdigit():
        print(have[int(check)])
    else:
        print(have[check])
