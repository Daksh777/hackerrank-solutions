size = int(input())
nums = [int(x) for x in input().split()]
positive = 0
negative = 0
zeroes = 0

for i in range(size):
    if nums[i] > 0:
        positive += 1
    if nums[i] == 0:
        zeroes += 1
    if nums[i] < 0:
        negative += 1

print(round(positive/size, 6))
print(round(negative/size, 6))
print(round(zeroes/size, 6))
