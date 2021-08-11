num = int(input())

i = 1
while i <= num:
    cnt = 0
    if ('3' in str(i)) or ('6' in str(i)) or ('9' in str(i)):
        cnt += str(i).count('3')
        cnt += str(i).count('6')
        cnt += str(i).count('9')
        print('-'*cnt, end=' ')  

    else:
        print(i, end=' ')
    
    i += 1
