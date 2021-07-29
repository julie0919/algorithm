subject = int(input())
scores = input().split()

max_score = 0
for score in scores:
    if max_score < int(score):
        max_score = int(score)

total_score = 0
for score in scores:
    total_score += int(score) / int(max_score) * 100

avg_score = total_score / subject
print(avg_score)
