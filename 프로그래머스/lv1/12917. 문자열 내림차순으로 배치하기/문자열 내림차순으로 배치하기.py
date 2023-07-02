def solution(s):
    answer = ''
    a = []
    
    for i in range(0,len(s)):
            a.append(ord(s[i]))
            
    a.sort(reverse=True)
    
    for i in range(0,len(s)):
        answer+=chr(a[i])

    return answer