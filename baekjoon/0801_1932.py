n = int(input())

num_list = []
for i in range(n):
    num_list.append(list(map(int, input().split())))

for i in range(1, n):
    for j in range(i+1):
        if j == 0:
            num_list[i][j] = num_list[i-1][j] + num_list[i][j]
        
        elif i == j:
            num_list[i][j] = num_list[i-1][j-1] + num_list[i][j]
        else:
            num_list[i][j] = max(num_list[i-1][j] + num_list[i][j], num_list[i-1][j-1] + num_list[i][j])

print(max(num_list[n-1]))

