arr = list(input())
brr = list(input())
a = len(arr) # 12
b = len(brr) # 11

def pattern(i, j):
    x = 0
    while 1:
        if arr[i+x] != brr[j+x]:
            return x
        else:
            if i+x == a-1 or j+x == b-1:
                return x+1
        x += 1

Max = 0
for i in range(a):
    for j in range(b):
        Len = pattern(i, j)
        if Len > Max:
            Max = Len
            idx = i

print(*arr[idx:idx+Max], sep='')