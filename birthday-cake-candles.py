size = int(input())
candles = [int(x) for x in input().split()]
candles.sort()
large = candles[-1]
count = 0
for i in reversed(candles):
    if i < large:
        break
    count += 1
print(count)
