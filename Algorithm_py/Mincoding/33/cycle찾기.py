N = int(input())
arr = [0]*100

def findboss(M):
    if arr[ord(M)] == 0:
        return M
    boss = findboss(arr[ord(M)])
    arr[ord(M)] = boss
    return boss


def union(a, b):
    global flag
    aboss = findboss(a)
    bboss = findboss(b)
    if aboss == bboss:
        return 1
    arr[ord(bboss)] = aboss


flag = 0
for _ in range(N):
    a, b = input().split()
    flag = union(a, b)
    if flag:
        break

print('발견' if flag else '미발견')