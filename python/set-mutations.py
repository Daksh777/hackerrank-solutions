n = int(input())
a = set(map(int, input().split()))
for i in range(int(input())):
    operator, num = input().split()
    b = set(map(int, input().split()))
    if operator == "intersection_update":
        a.intersection_update(b)
    elif operator == "update":
        a.update(b)
    elif operator == "symmetric_difference_update":
        a.symmetric_difference_update(b)
    elif operator == "difference_update":
        a.difference_update(b)

print(sum(a))