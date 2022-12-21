can, civ = map(int, input().split())
votes = []
names = []
for i in range(civ):
    a, b = input().split()
    votes.append(int(a))
    names.append(b)

bucket = [0] * 5
for i in range(len(votes)):
    bucket[votes[i]] += 1

winner = bucket.index(max(bucket))

for i in range(len(votes)):
    if votes[i] == winner:
        print(names[i], end=' ')



