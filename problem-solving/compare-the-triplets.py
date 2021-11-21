a = [int(i) for i in input().split()]
b = [int(i) for i in input().split()]

alice = 0
bob = 0
for x in range(3):
    if a[x] > b[x]:
        alice += 1
    elif a[x] == b[x]:
        continue
    elif a[x] < b[x]:
        bob += 1

print(alice, bob)
