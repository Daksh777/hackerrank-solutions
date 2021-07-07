n, k = [int(x) for x in input().split()] # bill[2] -> 6
bill = [int(x) for x in input().split()] # [2, 4, 6]
b = int(input())

total = sum(bill)
del bill[k]
later = sum(bill)/2

if b == later:
    print("Bon Appetit")
else:
    print(int(b-later))