move = [3, 2, 1, 3, 2, 'T', 1]
direct = ['R', 'R', 'L', 'R', 'L', 'T', 'L']
start = int(input())
def FindT(idx):
    if direct[idx] == 'T':
        return
    if direct[idx] == 'R':
        idx += move[idx]
    else:
        idx -= move[idx]
    FindT(idx)
    print(f'{idx}번')
FindT(start)
print(f'{start}번')

