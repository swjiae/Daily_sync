TC = int(input())
for T in range(1, TC+1):
    k, n, m = map(int, input().split())
    # k : 최대 이동 거리
    # n : 정류장 수
    # m : 충전소 수
    charge = list(map(int, input().split())) # 충전소 위치
    now = 0
    next = now + k
    cnt = 0
    while next < n:
        if next == now:
            cnt = 0
            break
        elif next in charge:
            now = next
            next = now + k
            cnt += 1
        else:
            next -= 1
    print(f'#{T} {cnt}')