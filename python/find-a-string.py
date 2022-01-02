string = input()
sub_string = input()
count = 0
for i in range(len(string)):
    if string[i:].startswith(sub_string):
        count += 1
print(count)
