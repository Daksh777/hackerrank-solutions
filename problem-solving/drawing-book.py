n = int(input())
p = int(input())

left = p//2

if n % 2 == 0:
    n += 1

right = (n-p)//2
print(min(left, right))