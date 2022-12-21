arr = [list(input()) for _ in range(4)]

brr = [
    ['A', 'B', 'C', 'D'],
    ['B', 'B', 'A', 'B'],
    ['C', 'B', 'A', 'C'],
    ['B', 'A', 'A', 'A']
]

dict_cnt = {}

for i in range(4):
    for j in range(4):
        if arr[i][j] == brr[i][j]:
            if arr[i][j] in dict_cnt:
                dict_cnt[arr[i][j]] += 1
            else:
                dict_cnt[arr[i][j]] = 1

Max = 0
for key, value in dict_cnt.items():
    if value > Max:
        Max = value
        result = key

print(result)
