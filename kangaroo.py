x1, v1, x2, v2 = [int(x) for x in input().split()]
if x1 == x2 and v1 == v2:
    print('YES')
elif v1 == v2:
    print('NO')
elif x1 > x2 and v1 > v2:
    print('NO')
elif x1 < x2 and v1 < v2:
    print('NO')
elif (x2-x1)%(v1-v2) == 0:
    print('YES')
else:
    print('NO')