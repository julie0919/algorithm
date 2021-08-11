T = int(input())

for tc in range(1, T+1):
    num_list = list(map(int, input().split()))

    maxV = num_list[0]
    for num in num_list:
        if maxV < num:
            maxV = num
    print('#{} {}'.format(tc, maxV))