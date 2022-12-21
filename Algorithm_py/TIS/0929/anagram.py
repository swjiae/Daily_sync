a = 'miles'
b = 'smile'

def anagram(a, b):
    a = list(a).sort()
    b = list(b).sort()
    print('anagram' if a == b else '아님')

anagram(a, b)

