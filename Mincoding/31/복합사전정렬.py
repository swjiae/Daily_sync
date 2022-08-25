n = int(input())
arr = list(input() for _ in range(n))
# arr.sort()
# brr = sorted(arr, key=lambda x: len(x)) # 1회성일 때 lambda 사용
#
# for i in range(n):
#     print(brr[i])

# 길이 짧은 순
result = sorted(arr, key=lambda x: (len(x), x))
# 길이 긴 순
result = sorted(arr, key=lambda x: (-len(x), x))





