N = input()

for i in range(len(N)//10):
    print(N[0:10])
    N = N[10:]

print(N)

    