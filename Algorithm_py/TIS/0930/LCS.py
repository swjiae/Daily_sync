str1 = list(input())
str2 = list(input())
N1 = len(str1)
N2 = len(str2)

arr = [[0]*(N1) for _ in range(N2)]

for y in range(N2):
    for x in range(N1):
        if str2[y] == str1[x]:
            arr[y][x] = arr[y-1][x-1] + 1

Max = 0
for y in arr:
    if max(y) > Max:
        Max = max(y)
print(Max)


'''
BABJYP
ABCBJY
'''