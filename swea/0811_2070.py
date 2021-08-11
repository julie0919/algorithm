T = int(input())

for tc in range(1, T+1):
    num = list(map(int, input().split()))

    if num[0] < num[1]:
        ans = '<'
    elif num[0] > num[1]:
        ans = '>'
    else:
        ans = '='
    print('#{} {}'.format(tc, ans))