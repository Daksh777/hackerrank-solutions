n = int(input())
arr = [int(x) for x in input().split()]
pairs = 0

d = {}
for i in arr:
    if i not in d:
        d[i] = 1
    else:
        d[i] += 1

for i in d.values():
    pairs += i//2
print(pairs)