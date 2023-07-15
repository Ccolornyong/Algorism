def solution(n, m):
    answer = []
    gcd = 1
    i = 2
    
    while(i<=n):
        if(n%i==0 and m%i==0):
            gcd*=i
            n=n//i
            m=m//i
            
        else:
            i+=1
             
    answer.append(gcd)
    answer.append(gcd*n*m)
    return answer