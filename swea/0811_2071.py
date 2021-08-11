import decimal

T = int(input())

for tc in range(1, T+1):
    num_list = list(map(int, input().split()))

    num_sum = 0
    for num in num_list:
        num_sum += num

    avg_num = round(decimal.Decimal(num_sum / len(num_list)), 0)
    print('#{} {}'.format(tc, avg_num))