import heapq

N = int(input())
arr = [int(input()) for _ in range(N)]
card = []
for i in range(len(arr)):
    heapq.heappush(card, arr[i])

answer = 0
while len(card) > 1:
    temp1 = heapq.heappop(card)
    temp2 = heapq.heappop(card)
    answer += temp1+temp2
    heapq.heappush(card, temp1+temp2)
