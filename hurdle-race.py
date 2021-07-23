n, k = map(int, input().split())
hurdles = [int(x) for x in input().split()]

if k >= max(hurdles):
    print(0)
else:
    print(max(hurdles)-k)