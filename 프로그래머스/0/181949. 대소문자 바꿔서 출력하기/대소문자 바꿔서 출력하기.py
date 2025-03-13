str = input()
for i in str:
    if i.islower():
        i = i.upper()
    else:
        i = i.lower()
    print(i, end="")