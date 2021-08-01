num = input()
if len(num) == 1:
    num = '0' + num
new_num = num

cycle_count = 0

while True:
    new_num = new_num[1] + str((int(new_num[0]) + int(new_num[1])) % 10)
    cycle_count += 1
    if(new_num == num):
        break

print(cycle_count)
    
