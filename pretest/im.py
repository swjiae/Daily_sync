TC = int(input())
for T in range(1, TC+1):
    N, Kmin, Kmax = map(int, input().split())
    scores = list(map(int, input().split()))
    Min = 21e8
    # T1, T2 가능한 조합
    for T1 in range(min(scores), max(scores)):
        for T2 in range(T1 + 1, max(scores) + 1):
            # 반 나누기
            A, B, C = [], [], []
            for i in scores:
                if i >= T2:
                    A.append(i)
                elif i >= T1:
                    B.append(i)
                else:
                    C.append(i)
            # 정원 확인
            total = []
            if Kmin <= len(A) <= Kmax and Kmin <= len(B) <= Kmax and Kmin <= len(C) <= Kmax:
                total.append(len(A))
                total.append(len(B))
                total.append(len(C))
            else: # 정원 미달 시
                result = -1
                continue
            # 정원 충족 시 Min 구하기
            tmp = max(total) - min(total)
            if tmp < Min:
                Min = tmp

    if Min != 21e8:
        result = Min
    print(f'#{T} {result}')
