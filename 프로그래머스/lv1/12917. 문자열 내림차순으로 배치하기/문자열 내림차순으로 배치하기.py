def solution(s):
    answer = ''
    a = []
    A = []
    n = []
    
    for i in range(0,len(s)):
        if (ord(s[i])>=97):
            a.append(ord(s[i]))
        else:
            A.append(ord(s[i]))
            
    a.sort(reverse=True)
    A.sort(reverse=True)
    
    n = a+A
    
    for i in range(0,len(s)):
        answer+=chr(n[i])

    return answer