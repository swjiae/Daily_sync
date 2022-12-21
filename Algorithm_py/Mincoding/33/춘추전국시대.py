N = int(input())
P = list(map(int, input().split()))
K = int(input())
group = [0]*100

def findboss(M):
    if group[ord(M)] == 0:
        return M
    boss = findboss(group[ord(M)])
    group[ord(M)] = boss
    return boss

def union(a, b):
    aboss = findboss(a)
    bboss = findboss(b)
    if aboss == bboss:
        return
    group[ord(bboss)] = aboss

def war(a, b):

    return

for i in range(K):
    s, a, b = input().split()
    if s == 'alliance':
        union(a, b)
    # else:
    #     war(a, b)

print(group)