def solution(s):
    answer = ''
    
    n=len(s)//2;
    
    if len(s)%2!=0:
        answer = s[n];
    else :
        answer = s[n-1]+s[n];
        
    return answer