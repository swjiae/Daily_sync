'''
숫자 2개 입력받고
최대공약수를 구하겠다 -> 2부터 둘 중 작은 수 까지 나누었을 때
나눠지는 수 중 가장 큰 수
32 16 / 16
24 16 / 8
'''
# 교수님 코드
# answer = 0
# a, b = map(int, input())
# for i in range(2, min(a, b)+1):
#     if a % i == 0 and b % i == 0:
#         answer = i
# print(answer)

'''
최대공약수를 위 코드보다 조금 더 빠른 속도로 구하고자 한다면?
유클리드호제법 (최초의 알고리즘이라는 것에 의미가 있음)
'''
a, b = map(int, input().split()) # 75 21
# 내 코드
while a and b:
    a, b = b, a % b
print(a)

# 교수님 코드
answer = 0
while b:
    answer = a % b
    a = b
    b = answer
print(a)

'''
최소공배수
'''