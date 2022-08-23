arr = [input() for _ in range(3)]

Max = 0
for i in arr:
    if len(i) > Max:
        Max = len(i)

brr = []
for n in range(len(arr)):
    if len(arr[n]) == Max:
        brr.append(arr[n])

flag = 0
for i in range(Max):
    for j in range(len(brr)-1):
        if brr[j][i] != brr[j+1][i]:
            if brr[j][i] > brr[j+1][i]:
                print(brr[j])
                flag = 1
                break
            else:
                print(brr[j+1])
                flag = 1
                break
    if flag:
        break