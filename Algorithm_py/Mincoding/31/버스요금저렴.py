fare = [1, 2, 3, 3, 5, 1, 0, 1, 3]
k = int(input())

start = 0
Sum = 0
Min = 21e8

for end in range(len(fare)):
    Sum += fare[end]
    if end >= k-1:
        if Sum < Min:
            Min = Sum
        Sum -= fare[start]
        start += 1

print(Min)
