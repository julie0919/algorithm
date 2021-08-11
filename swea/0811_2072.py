T = int(input())

for tc in range(1, T+1):
    num_list = list(map(int, input().split()))

    odd_sum = 0
    for num in num_list:
        if num % 2:
            odd_sum += num
    print('#{} {}'.format(tc, odd_sum))