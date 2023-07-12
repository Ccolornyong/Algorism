a, b = map(int, input().strip().split(' '))
c = ""

for i in range(b):
    for l in range(a):
        print("*", end="")
    print(" ")