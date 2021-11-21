size = int(input())
arr = [int(x) for x in input().split()]

maximum = 0

for i in arr:
    num = arr.count(i)
    prev = arr.count(i-1)
    total = num + prev
    if total > maximum:
        maximum = total
print(maximum)