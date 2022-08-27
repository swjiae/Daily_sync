word = list(input())
n = len(word)
# 문자를 숫자로 변경한 배열 생성
num = []
for i in range(n):
    num.append(ord(word[i]) - 64)

# 숫자를 문자로 변경하는 함수 만들기
def Change(arr):
    result = []
    for i in range(n):
        if arr[i] == '_':
            result.append(arr[i])
        else:
            result.append(chr(arr[i]+64))
    return result

# 1씩 감소시키며 출력하기
m = max(num)
for _ in range(m+1):
    print(''.join(Change(num)))
    for i in range(n):
        if num[i] != '_':
            num[i] -= 1
            if num[i] == 0:
                num[i] = '_'