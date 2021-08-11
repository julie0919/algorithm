T = int(input())

for tc in range(1, T+1):
    date = input()

    year = date[:4]
    mth = date[4:6]
    day = date[6:]
    result = ''
    
    if int(mth) in range(1, 13):
        if int(mth) % 2:
            if int(mth) < 8:
                if int(day) in range(1, 32):
                    result = year + '/' + mth + '/' + day
                else:
                    result = -1
            else:
                if int(day) in range(1, 31):
                    result = year + '/' + mth + '/' + day
                else:
                    result = -1
        else:
            if int(mth) > 7:
                if int(day) in range(1, 32):
                    result = year + '/' + mth + '/' + day
                else:
                    result = -1
            elif int(mth) > 2:
                if int(day) in range(1, 31):
                    result = year + '/' + mth + '/' + day
                else:
                    result = -1
            elif int(mth) == 2:
                if int(day) in range(1, 29):
                    result = year + '/' + mth + '/' + day
                else:
                    result = -1
    else:
        result = -1
    
    print('#{} {}'.format(tc, result))

