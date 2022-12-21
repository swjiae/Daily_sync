TC = int(input())
for T in range(1, TC+1):
    N, M = map(int, input().split()) # 컨테이너 수, 트럭 수
    w_con = list(map(int, input().split()))
    w_truck = list(map(int, input().split()))

    w_con.sort()
    w_truck.sort()

    Max = 0
    while w_con and w_truck:
        con, truck = w_con.pop(), w_truck.pop()
        if con <= truck:
            Max += con
        else:
            w_truck.append(truck)

    print(f'#{T} {Max}')