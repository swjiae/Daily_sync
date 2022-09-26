TC = int(input())
for T in range(1, TC+1):
    card = list(map(int, input().split()))

    # run 확인 함수
    def runn(p):
        p.sort()
        for j in range(len(p) - 2):
            if p[j] == p[j + 1] == p[j + 2]:
                return 1
        return 0

    # triplet 확인 함수
    def triplet(p):
        for j in range(len(p)):
            if p[j] in p and p[j]+1 in p and p[j]+2 in p:
                return 1
        return 0

    p1 = []
    p2 = []
    flag = 0
    flag2 = 0
    result = 0
    for i in range(len(card)):
        if i % 2 == 0:
            p1.append(card[i])
            if len(p1) >= 3:
                flag = runn(p1)
                flag2 = triplet(p1)
            if flag or flag2:
                result = 1
                break
        else:
            p2.append(card[i])
            if len(p2) >= 3:
                flag = runn(p2)
                flag2 = triplet(p2)
            if flag or flag2:
                result = 2
                break

    print(f'#{T} {result}')