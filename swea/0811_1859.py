T = int(input())

for tc in range(1, T+1):
    N = int(input())
    price = list(map(int, input().split()))

    price = price[::-1]
    maxp = price[0]
    bf = 0
    for i in range(1, len(price)):
        if maxp > price[i]:
            bf += maxp - price[i]
        else:
            maxp = price[i]
    print('#{} {}'.format(tc, bf))
    # s1   
    # bf = 0
    # buy = 0
    # cnt = 0
    # for i in range(N-1):
    #     if p[i] > p[i+1]:
    #         for p_high in p[i+2:]:
    #             if p_high > p[i]:
    #                 buy += p[i]
    #                 cnt += 1
    #                 break
    #         else:
    #             bf += p[i] * cnt - buy
    #             print(buy, cnt)
    #             buy = 0
    #             cnt = 0
                   

    #     elif p[i] < p[i+1]:
    #         buy += p[i]
    #         cnt += 1
    
    #     elif p[i] == p[i+1]:
    #         for p_high in p[i+2:]:
    #             if p_high > p[i]:
    #                 buy += p[i]
    #                 cnt += 1
    #                 break
    #         continue
    
    # bf += p[N-1] * cnt - buy

    # print('#{} {}'.format(tc, bf))