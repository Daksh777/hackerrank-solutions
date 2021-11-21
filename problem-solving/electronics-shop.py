b, n, m = map(int, input().split())
keyboards = [int(x) for x in input().split()]
drives = [int(x) for x in input().split()]

l = []

for keyboard in keyboards:
    for drive in drives:
        if keyboard + drive <= b:
            l.append(keyboard + drive)
        else:
            l.append(-1)
print(max(l))