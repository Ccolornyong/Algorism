def solution(left, right):
    answer = 0
    k = 1
    n = 0
    
    for i in range(left, right+1):
        for k in range(k,i+1):
            if(i%k==0):
                n+=1
        k=1
        if(n%2==0):
            answer+=i
        else:
            answer-=i
        n=0
    return answer