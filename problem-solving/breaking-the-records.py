input()
scores = [int(x) for x in input().split()]

maximum = scores[0]
minimum = scores[0]
max_count = 0
min_count = 0

for score in scores:
    if score > maximum:
        maximum = score
        max_count += 1
    
    if score < minimum:
        minimum = score
        min_count += 1
    
print(max_count, min_count)