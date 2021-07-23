n = int(input())
steps = input()
count = 0
valleys = 0
for i in steps:
    if i == "U":
        count += 1

    if i == "D":
        count -= 1
    
    if count == 0 and i=="U":
        valleys += 1

print(valleys)