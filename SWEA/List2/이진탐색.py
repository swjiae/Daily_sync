TC = int(input())
for T in range(1, TC+1):
    P, Pa, Pb = map(int, input().split()) # P: 총 page # PA: A target # PB: B target
    arr = [i for i in range(1, P+1)] # Page 배열
    L = 1
    R = P
    def BS(L, R, target):
        cnt = 0
        while 1:
            cnt += 1
            Mid = (L + R) // 2
            if Mid == target:
                return cnt
            elif Mid > target:
                R = Mid
            else:
                L = Mid

    if BS(L, R, Pa) < BS(L, R, Pb):
        winner = 'A'
    elif BS(L, R, Pa) > BS(L, R, Pb):
        winner = 'B'
    else:
        winner = 0

    print(f'#{T} {winner}')