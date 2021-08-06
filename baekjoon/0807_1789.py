num = int(input())

n = 1
while (n * (n + 1)) / 2 <= num:
    n += 1
print(n - 1)

# def sum_num(num_max):
#     s = 0
#     for i in range(1, num_max + 1):
#         s += i
#     return(s)

# j = 0
# while True:
#     if sum_num(j) < num:
#         j += 1
#     elif sum_num(j) > num:
#         print(j - 1)
#         break
#     elif sum_num(j) == num:
#         print(j)
#         break
    