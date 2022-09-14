TC = int(input())
for T in range(1, TC + 1):  # 1

    # 인접 리스트 만들기 + 확인할 노드 입력 받기
    V, E = map(int, input().split())  # 6, 5
    arr = [[] for _ in range(V)]  # [[3, 2], [2, 4], [], [5], [], []]
    for _ in range(E):
        P, C = map(int, input().split())  # 1, 4 ...
        arr[P - 1].append(C - 1)
    S, G = map(int, input().split())  # 1, 6

    # 경로 존재 여부 확인하기
    flag = 0
    end = G - 1

    def dfs(start):
        global flag, end
        stack = [start]
        used = []
        while stack:
            node = stack.pop()
            if node not in used:
                used.append(node)
                for i in range(len(arr[node])):
                    stack.append(arr[node][i])
        if end in used:
            flag = 1

    dfs(S - 1)

    # 결과 출력하기
    print(f'#{T} {flag}')