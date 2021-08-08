numbers = map(int, input().split())

up = numbers[0]
down = numbers[1]
height = numbers[2]

n = 0
while True:
    if (up - down) * n + up >= height:
        print(n + 1)
        break
    else:
        n += 1