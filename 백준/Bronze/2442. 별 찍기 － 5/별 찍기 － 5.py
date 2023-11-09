N = int(input())

for l in range(N): # line
    for b in range(N-(l+1)):
        print(" ", end="")
    for s in range(l+1): # star
        print("*", end="")

    for s in range(l): # star
        print("*", end="")

    print("")    