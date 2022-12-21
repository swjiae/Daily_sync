arr = list(input())
st = 0
ed = 9
while 1:
    mid = (st+ed)//2
    if st >= ed:
        print(f'{st*10}%')
        break
    if arr[mid] == '#':
        st = mid + 1
    if arr[mid] == '_':
        ed = mid - 1