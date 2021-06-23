int(input())
arr = [int(x) for x in input().split()]
count = [0] * (len(arr)+1)
for i in range(len(arr)):
    count[arr[i]] += 1
print(count.index(max(count)))