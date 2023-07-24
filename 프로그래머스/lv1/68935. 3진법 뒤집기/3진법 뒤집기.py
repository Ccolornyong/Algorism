def solution(n):
    answer = 0
    num = ""
    while n!=0:
        num+=(str)(n%3)
        n=n//3
    num=num[::-1]
    legth=len((str)(num))
    for i in range(legth-1,-1,-1): 
        answer+=(3**i)*(int)(num[i])
    
    return answer