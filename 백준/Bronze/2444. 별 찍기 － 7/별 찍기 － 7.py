N = int(input())

for l in range((N*2)//2): # line
    
    for b in range(N-(l+1)): # blank
        print(" ", end="")
    
    for s in range(l+1):
        print("*", end="")

    for s in range(l):
        print("*", end="")

    print(" ")

for l in range((N*2)-1):

    for b in range(l+1): # blank
        print(" ", end="")
    
    for s in range(N-(l+1)): # blank
        print("*", end="")

    for s in range(N-(l+2)): # blank
        print("*", end="")

    print(" ")