# Bubble Sort

N = int(input())
scores = list(map(int, input().split()))

for i in range(N-1):
    for j in range(N-1-i):
        if scores[j] > scores[j+1]:
            scores[j], scores[j+1] = scores[j+1], scores[j]

mid = scores[N//2]
print(mid)