TC = int(input())
for T in range(1, TC+1):
    N, M, L = map(int, input().split())
    tree = [0] * (N+1)
    for i in range(M):
        idx, value = map(int, input().split())
        tree[idx] += value

    for i in range(N, L-1, -1):
        parent = i // 2
        tree[parent] += tree[i]

    print(f'#{T} {tree[L]}')

