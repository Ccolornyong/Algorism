def solution(a, b, c, d):
    listall = [a,b,c,d]
    setall = set(listall)
    answer, p, q = 0, 0, 0
    
    if len(setall) == 1:
        p = list(setall)[0]
        answer = 1111*p
        
    elif len(setall) == 2:
        if listall.count(list(setall)[0])==2:
            p,q = list(setall)[0], list(setall)[1]
            answer = (p+q)*abs(p-q)
        else:
            if listall.count(list(setall)[0])==3:
                p,q = list(setall)[0], list(setall)[1]
            else:
                p,q = list(setall)[1], list(setall)[0]
            answer = (10*p+q)**2
            
    elif len(setall) == 3:
        for i in range(len(setall)):
            if listall.count(list(setall)[i])==2:
                p = list(setall)[i]
        setall.remove(p)
        q = list(setall)[0]
        r = list(setall)[1]
        answer = q*r
        
    elif len(setall) == 4:
        answer = min(listall)
        
    return answer