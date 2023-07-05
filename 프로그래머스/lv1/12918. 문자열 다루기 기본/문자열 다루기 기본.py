def solution(s):
    answer = True
    
    if(len(s)==4 or len(s)==6):
        for i in range(len(s)):
            if(ord(s[i])<48 or ord(s[i])>57):
                answer=False
               
    else:
        answer=False
                
    return answer