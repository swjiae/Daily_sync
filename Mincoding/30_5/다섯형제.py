# # level = 5
# # brunch = 2
#
# arr = sorted(list(map(int, input().split()))) # 1, 3, 4, 5, 9
# path = [0] * 5
# cnt = 0
# sum = 0
# def abc(level):
#     global cnt, sum
#     if level == 5:
#         return
#     for i in range(5):
#         if level > 0 and path[level-1] >= arr[i]: continue
#         path[level] = arr[i]
#         sum += path[i]
#         if 10 <= sum <= 20:
#             cnt += 1
#         abc(level+1)
#         sum -= path[i]
#
# abc(0)
# print(cnt)

arr = list(map(int,input().split()))
path = [0]*10
cnt = 0
sum = 0
def abc(level):
    global cnt,path,sum

    sum = 0

    for i in range(level):
        sum += path[i]
    if sum >= 10 and 20 >= sum:
        cnt += 1

    if level == len(arr):
        return

    for i in range(len(arr)):
        if level>0 and path[level-1] >= arr[i]:
            continue
        path[level] = arr[i]
        abc(level+1)

abc(0)
print(cnt)