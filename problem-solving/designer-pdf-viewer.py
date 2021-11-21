from string import ascii_lowercase

x = [int(i) for i in input().split()]
word = input()
numbers = {}
for i, num in enumerate(x):
    letter = ascii_lowercase[i]
    numbers[letter] = num
    
large = 0    
for i in word:
    if numbers[i] >= large:
        large = numbers[i]
print(large*len(word))