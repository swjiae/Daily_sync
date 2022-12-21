arr = [
    [0, 0, 1, 0, 2, 1], # 0
    [5, 0, 3, 0, 0, 0], # 1
    [0, 0, 0, 0, 0, 7], # 2
    [2, 0, 0, 0, 8, 0], # 3
    [0, 0, 9, 0, 0, 0], # 4
    [4, 0, 0, 7, 0, 0]  # 5
]

start = int(input())

def dfs(start):
    stack = [start]
    used = []
    cum = [0]
    sum = 0
    outdict = {}
    while stack:
        node = stack.pop()
        sum += cum.pop()
        if node not in used:
            used.append(node)
            outdict[node] = sum
            for i in range(len(arr[node]) - 1, -1, -1):
                if arr[node][i] >= 1 and i not in used:
                    stack.append(i)
                    cum.append(arr[node][i])
    for key, value in outdict.items():
        print(key, value)

dfs(start)