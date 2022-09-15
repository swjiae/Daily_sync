arr = [0]*100

def findboss(M):
    if arr[ord(M)] == 0:
        return M
    boss = findboss(arr[ord(M)])
    arr[ord(M)] = boss
    return boss

def union(a, b):
    aboss = findboss(a)
    bboss = findboss(b)
    if aboss == bboss: return
    arr[ord(bboss)] = aboss

union('A', 'B')
union('A', 'C')
union('D', 'E')
union('D', 'F')
union('G', 'H')
union('I', 'J')

N = int(input())
for _ in range(3):
    a, b = input().split()
    union(a, b)

cnt = 0
for i in range(ord('A'), ord('J')+1):
    if arr[i] == 0:
        cnt += 1

print(f'{cnt}개')