l = []
for i in range(int(input())):
    operation, *num = input().split()
    if operation == "print":
        print(l)
    elif operation == "insert":
        l.insert(int(num[0]), int(num[1]))
    elif operation == "remove":
        l.remove(int(*num))
    elif operation == "append":
        l.append(int(*num))
    elif operation == "sort":
        l.sort()    
    elif operation == "pop":
        l.pop()
    else:
        l.reverse()