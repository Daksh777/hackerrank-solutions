chocolates = int(input())
bar = [int(x) for x in input().split()]
d, m = [int(x) for x in input().split()]

count = 0

for i in range(len(bar) - m + 1):
    nums = bar[i:i+m]
    if sum(nums) == d:
        count += 1

print(count)