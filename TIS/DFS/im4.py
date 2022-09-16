'''
multi를 전역으로 선언 후
원상복구를 할때
'''

arr = [7, 3, 5, 4]
Max = 0
def dfs(level):
    global Max
    if level == 4:
        multi = 1
        for i in range(4):
            multi *= arr[i]
            Max = max(Max, multi)
        return

    backup = arr[level]

    arr[level] *= 2
    dfs(level+1)
    arr[level] = backup

    arr[level] //= 3
    dfs(level+1)
    arr[level] = backup

    arr[level] += 5
    dfs(level+1)
    arr[level] = backup

dfs(0)
print(Max)