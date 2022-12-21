cand = list(input()) # brunch
elec = 2 # level
path = [''] * 2
def abc(level):
    if level == 2:
        for i in range(level):
            print(path[i], end='')
        print()
        return
    for i in range(len(cand)):
        path[level] = cand[i]
        abc(level+1)

abc(0)