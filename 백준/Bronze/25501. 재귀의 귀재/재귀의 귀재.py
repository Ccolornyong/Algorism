T = int(input())

global num

def recursion(s, l, r):
    global num
    num+=1
        
    if l >= r: return 1
    elif s[l] != s[r]: return 0
    else: 
        return recursion(s, l+1, r-1)

def isPalindrome(s):
    return recursion(s, 0, len(s)-1)

for i in range(T):
    s = input()
    num = 0
    print(isPalindrome(s), num)