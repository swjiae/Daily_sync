TC = int(input())
for T in range(1, TC+1):
    K, N, M = map(int, input().split())
    mrr = list(map(int, input().split()))
    now = K
    cnt = 0
    while now != N:
        if cnt > M:
            cnt = 0
            break
        elif now in mrr:
            now += K
            cnt += 1
        else:
            now -= 1
    print(f'#{T} {cnt}')