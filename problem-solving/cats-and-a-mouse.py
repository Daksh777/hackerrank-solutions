q = int(input())
for i in range(q):
    x, y, z = map(int, input().split())
    if abs(x-z) == abs(y-z):
        print("Mouse C")
    elif abs(x-z) < abs(y-z):
        print("Cat A")
    else:
        print("Cat B")