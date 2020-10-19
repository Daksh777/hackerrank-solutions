size = int(input())
nums = []
for i in range(size):
    nums.append([int(x) for x in input().split()])
sum1 = sum(nums[i][i] for i in range(size))
sum2 = sum(nums[i][-i-1] for i in range(size))
ans = abs(sum1 - sum2)
print(ans)
