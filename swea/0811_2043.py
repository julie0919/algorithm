P, K = map(int, input().split())

cnt = 0
while True:
    if P != K:
        K += 1
        cnt += 1
    else:
        break

print(cnt+1)