arr = [
    [0, 1, 0, 0, 1, 0],
    [0, 0, 1, 0, 0, 1],
    [0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0]
]

start = int(input())

def bfs(start):
    stack = [start]
    while stack:
        node = stack.pop(0)
        print(node, end = ' ')
        for i in range(len(arr)):
            if arr[node][i] == 1:
                stack.append(i)

bfs(start)