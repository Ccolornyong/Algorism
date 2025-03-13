str = input()
print(''.join(i.upper() if i == i.lower() else i.lower() for i in str))