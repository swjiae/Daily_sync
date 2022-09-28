def palindrome(string):


    return

TC = int(input())
for T in range(1, TC+1):
    N, M = map(int, input().split()) # 배열크기, 회문크기
    arr = [list(input()) for _ in range(N)]
    for i in range(N):
        for j in range(N-M+1):
            palindrome(arr[i][j:j+M]) # 행 확인
            palindrome() # 열 확인

'''
GOFFAKWFSM
OYECRSLDLQ
UJAJQVSYYC
JAEZNNZEAJ !
WJAKCGSGCF
QKUDGATDQL
OKGPFPYRKQ
TDCXBMQTIO
UNADRPNETZ
ZATWDEKDQF
'''