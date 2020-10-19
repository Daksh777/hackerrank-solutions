nums = [int(x) for x in input().split()]
s = sum(nums)

large = s-nums[0]
small = s-nums[0]

for num in nums:
    if s-num < small:
        small = s-num
    if s-num > large:
        large = s-num
print(small, large)
