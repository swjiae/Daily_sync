arr = ['BTS', 'SBS', 'BS', 'CBS', 'SES']
Min = 21e8
path = ['']*100
target = input()

def dfs(level, cnt):
    global Min
    str = ''.join(path)
    if str == target:
        Min = min(Min, cnt)
        return
    if len(str) > len(target):
        return
    for i in range(5):
        path[level] = arr[i]
        dfs(level+1, cnt+1)
        path[level] = ''

dfs(0, 0)
print(Min)