def solution(a, d, included):
    result = 0
    
    for i, flag in enumerate(included):
        if flag == 1:
            result += a+d*i
        
    return result