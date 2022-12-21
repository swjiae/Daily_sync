arr = list(input())
n = int(input()) # 뽑을 카드 개수

arr.sort(reverse=True)
brr = arr[0:n]
# brr = []
# for i in range(n):
#     brr.append(arr[i])

result = sorted(brr, key=lambda x: -brr.count(x))
print(result[0])
