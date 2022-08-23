# level = int(input())
# brunch = 2

people = int(input())
arr = ['o', 'x']
path = ['']*4
def abc(level):
    if level == people:
        for i in range(level):
            print(path[i], end='')
        print()
        return
    for i in range(2):
        path[level] = arr[i]
        abc(level+1)

abc(0)