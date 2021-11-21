input()
a = [int(x) for x in input().split()]
b = [int(x) for x in input().split()]

common_factors = None

for num in b:
    factors = set()
    for x in range(1, num+1):
        if num % x == 0:
            factors.add(x)

    if common_factors is None:
        common_factors = factors
    else:
        common_factors = factors.intersection(common_factors)

count = 0
for f in common_factors:
    if all(f % x == 0 for x in a):
        count += 1

print(count)