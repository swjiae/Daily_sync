a = list(input())
b = list(input()) # 기준

# sort로 anagram 찾기

# def anagram(tmp):
#     tmp.sort()
#     a.sort()
#     if a == tmp:
#         return 1
#     return 0
# ---------------------------------------------------

# dat로 anagram 찾기

def dat(tmp):
    budget1 = [0]*20
    budget2 = [0]*20
    for i in tmp:
        budget1[ord(i)-ord('a')] += 1
    for i in a:
        budget2[ord(i)-ord('a')] += 1

    flag = 1
    for i in range(20):
        if budget1[i] != budget2[i]:
            flag = 0
    if flag:
        return 1
    return 0
# ---------------------------------------------------

# slicing으로 확인하기

# cnt = 0
# for i in range(len(b)-len(a)+1):
#     tmp = b[i:i+len(a)]
#     cnt += dat(tmp)
# print(cnt)
# ---------------------------------------------------

'''
abcab
aabbcbbaa
'''

