def solution(A,B):
    answer = 0
    ans = 0

    A = sorted(A)
    B = sorted(B, reverse = True)
    
    for i in range(len(A)):
        ans = A[i]*B[i]
        answer+=ans
        
    return answer