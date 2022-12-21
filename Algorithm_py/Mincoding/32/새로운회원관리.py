n = int(input())
names = list(input() for _ in range(n))

def iscapitalize(name):
    if name[0].isupper():
        if name[1:len(name)-1].islower():
            return 1
    return 0

for i in range(n):
    # capitalized 경우
    if iscapitalize(names[i]):
        continue
    # 소문자로만 되어있는 경우
    if names[i].islower():
        names[i] = names[i].capitalize()
    #  mixed 경우
    else:
        names[i] = names[i].upper()

for i in range(n):
    print(sorted(names)[i])
