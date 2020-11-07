s, t = (int(i) for i in input().split())
a, b = (int(i) for i in input().split())
m, n = (int(i) for i in input().split())
apple = [int(i) for i in input().split()]
orange = [int(i) for i in input().split()]
count = 0

for i in range(m):
    final_distance = apple[i] + a
    if s <= final_distance <= t:
        count += 1
print(count)
count=0
for i in range(n):
    final_distance = orange[i] + b
    if s <= final_distance <= t:
        count += 1
print(count)