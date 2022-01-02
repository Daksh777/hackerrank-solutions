s = input()
position, new_character = input().split()
print(s[:int(position)] + new_character + s[int(position)+1:])