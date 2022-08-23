arr = [
    [0, 0, 1, 1, 0, 1],
    [0, 0, 0, 1, 1, 1],
    [0, 0, 0, 0, 1, 1],
    [0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 0]
]

start = int(input())

def dfs(start):
    stack = [start]
    visit = []

    while stack:
        node = stack.pop()
        if node not in visit:
            visit.append(node)
            for i in range(len(arr[node])-1, -1, -1):
                if arr[node][i] == 1:
                    stack.append(i)
    print(*visit)


dfs(start)