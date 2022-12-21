name = ['Amy', 'Bob', 'Chole', 'Diane', 'Edger']
tree = [
    [0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0],
    [0, 1, 0, 0, 0],
    [0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0],
]

# 부모 cnt max?
Max = 0
for i in range(5):
    cnt = 0
    for j in range(5):
        if tree[j][i] == 1:
            cnt += 1
    if Max < cnt:
        Max = cnt
        result = i

print(name[result])

