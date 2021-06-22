n, k = map(int,input().split())
arr = [int(x) for x in input().split()]
count = 0

for i in range(n):
    for j in range(i+1, n):
        if (arr[i] + arr[j]) % k == 0:
            count += 1
print(count)
