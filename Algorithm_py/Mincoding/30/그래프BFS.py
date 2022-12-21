arr = [
    [0, 0, 0, 0, 1, 0],
    [1, 0, 1, 0, 0, 1],
    [1, 0, 0, 1, 0, 0],
    [1, 1, 0, 0, 0, 0],
    [0, 1, 0, 1, 0, 1],
    [0, 0, 1, 1, 0, 0]
]

start = int(input())

def bfs(start):
    queue = [start]
    used = []
    while queue:
        node = queue.pop(0)
        if node not in used:
            used.append(node)
            for i in range(len(arr)):
                if arr[node][i] == 1:
                    queue.append(i)
    for i in range(len(used)):
        print(used[i])

bfs(start)