num = int(input())

cnt = 0
while True:
    if not bool(num % 5):
        cnt += num // 5
        print(cnt)
        break
    num -= 3
    cnt += 1

    if num < 0:
        print(-1)
        break
        




# cnt = 0
# while num:
#     if num == 1 or num == 2 or num == 4 or num == 7:
#         print(-1)
#         break
#     elif not bool(num % 5):
#         cnt += num // 5
#         print(cnt)
#         break
#     elif not bool((num % 5) % 3):
#         cnt += num // 5
#         cnt += (num % 5) // 3
#         print(cnt)
#         break
#     else:
#         cnt += num // 3
#         print(cnt)
#         break