n = int(input())
arr = list(map(int, input().split()))
arr.sort()
print(max(n for n in arr if n!=max(arr)))