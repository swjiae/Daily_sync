n = int(input())
arr = ['B', 'I', 'A', 'H']
idx = 0
while arr:
    selected = n % len(arr)
    idx = idx + selected - 1
    hero = arr[idx]
    print(hero, end=' ')
    arr.pop(idx)
