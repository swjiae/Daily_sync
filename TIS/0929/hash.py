from collections import Counter
participant = ["leo", "kiki", "eden"]
completion = ["eden", "kiki"]
result = Counter(participant) - Counter(completion)
print(result)
for i in result.items():
    print(i[0])
