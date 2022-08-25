P = 123

P = P * 2
print(P)
P = list(str(P))
print(P)
for i in range(len(P)%2):
    P[i], P[-i-1] = P[-i-1], P[i]
print(P)
P = ''.join(P)
print(P)
