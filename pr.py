n=4
arr=[7,3,5,4]
Max=-21e8

def dfs(level,gop):
    global Max
    if level==4:
        Max=max(Max,gop)
        return
    dfs(level+1,gop*(arr[level]*2))
    dfs(level+1,gop*(arr[level]//3))
    dfs(level+1,gop*(arr[level]+5))

dfs(0,1)
print(Max)